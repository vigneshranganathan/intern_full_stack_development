from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from qa_app.models import Question, Answer, UserProfile
from qa_app.chatgpt_integration import ChatGPTIntegration

class Command(BaseCommand):
    help = 'Populate database with sample data for testing'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10, help='Number of users to create')
        parser.add_argument('--questions', type=int, default=10, help='Number of questions to create')

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Sample user data
        sample_users = [
            {'username': 'electrical_engineer', 'email': 'ee@example.com', 'first_name': 'John', 'last_name': 'Engineer'},
            {'username': 'motor_expert', 'email': 'motor@example.com', 'first_name': 'Sarah', 'last_name': 'Motors'},
            {'username': 'power_systems', 'email': 'power@example.com', 'first_name': 'Mike', 'last_name': 'Power'},
            {'username': 'transformer_tech', 'email': 'transformer@example.com', 'first_name': 'Lisa', 'last_name': 'Tech'},
            {'username': 'control_systems', 'email': 'control@example.com', 'first_name': 'David', 'last_name': 'Control'},
            {'username': 'ac_motor_specialist', 'email': 'ac@example.com', 'first_name': 'Anna', 'last_name': 'AC'},
            {'username': 'dc_motor_pro', 'email': 'dc@example.com', 'first_name': 'Bob', 'last_name': 'DC'},
            {'username': 'generator_guru', 'email': 'gen@example.com', 'first_name': 'Carol', 'last_name': 'Generator'},
            {'username': 'power_electronics', 'email': 'pe@example.com', 'first_name': 'Dan', 'last_name': 'Electronics'},
            {'username': 'machine_designer', 'email': 'designer@example.com', 'first_name': 'Eve', 'last_name': 'Designer'},
        ]
        
        # Create users
        created_users = []
        for i, user_data in enumerate(sample_users[:options['users']]):
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'is_active': True,
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                
                UserProfile.objects.get_or_create(
                    user=user,
                    defaults={
                        'bio': f'Experienced professional in electrical machines and power systems.',
                        'expertise_level': ['BEGINNER', 'INTERMEDIATE', 'ADVANCED', 'EXPERT'][i % 4]
                    }
                )
                created_users.append(user)
                self.stdout.write(f'Created user: {user.username}')
        
        # Sample questions
        sample_questions = [
            {
                'title': 'What is the difference between synchronous and asynchronous motors?',
                'content': 'I am studying electrical machines and I am confused about the fundamental differences between synchronous and asynchronous motors. Can someone explain the key differences in terms of operation, applications, and performance characteristics?',
                'category': 'AC_MOTORS'
            },
            {
                'title': 'How to calculate the efficiency of a transformer?',
                'content': 'I need to calculate the efficiency of a 500 KVA transformer. What are the losses involved and what is the standard method for efficiency calculation?',
                'category': 'TRANSFORMERS'
            },
            {
                'title': 'DC motor speed control methods',
                'content': 'What are the different methods available for controlling the speed of DC motors? Which method is most efficient for industrial applications?',
                'category': 'DC_MOTORS'
            },
            {
                'title': 'Generator vs Motor operation modes',
                'content': 'Can the same electrical machine work as both a generator and a motor? What changes are needed to switch between these modes?',
                'category': 'GENERATORS'
            },
            {
                'title': 'Power factor correction in motors',
                'content': 'Why do induction motors have poor power factor and how can we improve it? What are the methods used for power factor correction?',
                'category': 'AC_MOTORS'
            },
            {
                'title': 'Transformer cooling methods',
                'content': 'What are the different cooling methods used in power transformers? How do we choose the appropriate cooling method for different ratings?',
                'category': 'TRANSFORMERS'
            },
            {
                'title': 'Starting methods for induction motors',
                'content': 'What are the various starting methods for three-phase induction motors? When should each method be used?',
                'category': 'AC_MOTORS'
            },
            {
                'title': 'DC generator characteristics',
                'content': 'Can you explain the different types of DC generators and their characteristic curves? How do they differ in performance?',
                'category': 'GENERATORS'
            },
            {
                'title': 'Motor protection systems',
                'content': 'What are the essential protection systems required for industrial motors? How do overload and short circuit protection work?',
                'category': 'CONTROL_SYSTEMS'
            },
            {
                'title': 'Inverter drive applications',
                'content': 'How do variable frequency drives work and what are their main applications in industry? What are the advantages over traditional control methods?',
                'category': 'POWER_ELECTRONICS'
            },
        ]
        
        # Create questions with answers
        chatgpt = ChatGPTIntegration()
        for i, question_data in enumerate(sample_questions[:options['questions']]):
            if created_users:
                author = created_users[i % len(created_users)]
            else:
                author = User.objects.first()
                
            question, created = Question.objects.get_or_create(
                title=question_data['title'],
                defaults={
                    'content': question_data['content'],
                    'category': question_data['category'],
                    'author': author
                }
            )
            
            if created:
                self.stdout.write(f'Created question: {question.title}')
                
                # Generate answer using ChatGPT
                try:
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
                        self.stdout.write(f'Generated answer for: {question.title}')
                    else:
                        # Create a basic answer if AI fails
                        Answer.objects.create(
                            question=question,
                            content="This is a sample answer. To get AI-generated answers, please configure your OpenAI API key in the .env file.",
                            source="Sample Data",
                            confidence_score=0.5
                        )
                        self.stdout.write(f'Created sample answer for: {question.title}')
                        
                except Exception as e:
                    self.stdout.write(f'Error generating answer: {str(e)}')
                    # Create a basic answer as fallback
                    Answer.objects.create(
                        question=question,
                        content="This is a sample answer. To get AI-generated answers, please configure your OpenAI API key in the .env file.",
                        source="Sample Data",
                        confidence_score=0.5
                    )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created sample data!')
        )