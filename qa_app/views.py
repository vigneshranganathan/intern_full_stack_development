from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import logging

from .models import Question, Answer, UserProfile, QuestionView
from .forms import CustomUserCreationForm, QuestionForm, UserProfileForm
from .chatgpt_integration import ChatGPTIntegration

logger = logging.getLogger(__name__)

def home(request):
    recent_questions = Question.objects.select_related('author').prefetch_related('answer')[:6]
    total_questions = Question.objects.count()
    answered_questions = Question.objects.filter(answer__isnull=False).count()
    total_users = User.objects.count()
    
    category_stats = Question.objects.values('category').annotate(
        count=Count('id')
    ).order_by('-count')
    
    context = {
        'recent_questions': recent_questions,
        'total_questions': total_questions,
        'answered_questions': answered_questions,
        'total_users': total_users,
        'category_stats': category_stats,
    }
    return render(request, 'home.html', context)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Electrical Machines Q&A!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def ask_question_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            
            try:
                chatgpt = ChatGPTIntegration()
                if chatgpt.is_electrical_machines_related(question.content):
                    result = chatgpt.get_answer(
                        question.title, 
                        question.content, 
                        question.get_category_display()
                    )
                    
                    if result['success']:
                        Answer.objects.create(
                            question=question,
                            content=result['answer'],
                            source=result['source'],
                            confidence_score=result['confidence_score']
                        )
                        messages.success(request, 'Question submitted successfully and answer generated!')
                    else:
                        messages.warning(request, 'Question submitted, but there was an issue generating the AI answer.')
                else:
                    Answer.objects.create(
                        question=question,
                        content="This question doesn't appear to be directly related to electrical machines. Please ask questions about DC/AC motors, transformers, generators, or other electrical machine topics for the best answers.",
                        source="System",
                        confidence_score=0.5
                    )
                    messages.info(request, 'Question submitted. For best results, please ask questions related to electrical machines.')
                    
            except Exception as e:
                logger.error(f"Error generating answer for question {question.id}: {str(e)}")
                messages.warning(request, 'Question submitted successfully, but answer generation failed. Please try again later.')
            
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    
    return render(request, 'ask_question.html', {'form': form})


def question_detail_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.user.is_authenticated:
        QuestionView.objects.get_or_create(
            question=question,
            user=request.user,
            ip_address=get_client_ip(request)
        )
    
    related_questions = Question.objects.filter(
        category=question.category
    ).exclude(pk=question.pk).select_related('author')[:5]
    
    context = {
        'question': question,
        'related_questions': related_questions,
    }
    return render(request, 'question_detail.html', context)

def questions_list_view(request):
    questions = Question.objects.select_related('author').prefetch_related('answer')
    
    search_query = request.GET.get('search')
    if search_query:
        questions = questions.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    category = request.GET.get('category')
    if category:
        questions = questions.filter(category=category)
    
    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Question.CATEGORY_CHOICES
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category,
        'search_query': search_query,
    }
    return render(request, 'questions_list.html', context)

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    user_questions = Question.objects.filter(author=request.user).order_by('-created_at')[:5]
    
    context = {
        'form': form,
        'profile': profile,
        'user_questions': user_questions,
    }
    return render(request, 'profile.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@require_POST
@login_required
def regenerate_answer_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.user != question.author and not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Permission denied'})
    
    try:
        chatgpt = ChatGPTIntegration()
        result = chatgpt.get_answer(
            question.title, 
            question.content, 
            question.get_category_display()
        )
        
        if result['success']:
            answer, created = Answer.objects.get_or_create(
                question=question,
                defaults={
                    'content': result['answer'],
                    'source': result['source'],
                    'confidence_score': result['confidence_score']
                }
            )
            
            if not created:
                answer.content = result['answer']
                answer.source = result['source']
                answer.confidence_score = result['confidence_score']
                answer.save()
            
            return JsonResponse({
                'success': True,
                'answer': result['answer'],
                'confidence_score': result['confidence_score']
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Failed to generate answer'
            })
            
    except Exception as e:
        logger.error(f"Error regenerating answer: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Internal server error'
        })