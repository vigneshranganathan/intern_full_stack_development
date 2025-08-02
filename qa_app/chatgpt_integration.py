from openai import OpenAI
import logging
from django.conf import settings
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class ChatGPTIntegration:
    def __init__(self):
        
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else None
    
    def get_answer(self, question_title: str, question_content: str, category: str) -> Dict[str, any]:
        if not self.client:
            return {
                'success': False,
                'answer': 'OpenAI API key not configured. Please add your API key to continue.',
                'confidence_score': 0.0,
                'source': 'Error',
                'error': 'API key not configured'
            }
        
        try:
            system_prompt = '''You are an expert in electrical machines and power systems. 
            Provide accurate, detailed, and technical answers about electrical machines including:
            - DC and AC motors, Transformers, Generators, Power electronics, Control systems
            
            Always include:
            1. Clear technical explanation
            2. Relevant formulas when applicable
            3. Practical applications
            4. Safety considerations when relevant'''
            
            user_prompt = f'''Question Category: {category}
Question Title: {question_title}
Question Details: {question_content}

Please provide a comprehensive answer about this electrical machines topic.'''
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=1500,
                temperature=0.3,
            )
            
            answer_content = response.choices[0].message.content
            confidence_score = min(len(answer_content) / 1000, 1.0)
            
            return {
                'success': True,
                'answer': answer_content,
                'confidence_score': confidence_score,
                'source': 'OpenAI GPT-3.5-turbo',
                'tokens_used': response.usage.total_tokens if response.usage else 0
            }
            
        except Exception as e:
            logger.error(f"Error getting ChatGPT response: {str(e)}")
            return {
                'success': False,
                'answer': 'Sorry, I encountered an error while generating the answer. Please try again later.',
                'confidence_score': 0.0,
                'source': 'Error',
                'error': str(e)
            }
    
    def is_electrical_machines_related(self, question: str) -> bool:
        electrical_keywords = [
            'motor', 'generator', 'transformer', 'electrical', 'power', 'voltage',
            'current', 'circuit', 'induction', 'synchronous', 'dc', 'ac', 'magnetic'
        ]
        question_lower = question.lower()
        return any(keyword in question_lower for keyword in electrical_keywords)