import json
from django.core.management.base import BaseCommand
from basicapp.models import QuizQuestion

class Command(BaseCommand):
    help = 'Import quiz questions from a JSON file'

    def handle(self, *args, **kwargs):
        with open('path/to/your/questions.json') as f:
            data = json.load(f)

        for question_data in data:
            question = QuizQuestion(
                summary=question_data['summary'],
                image=question_data['image'],
                details=question_data['details'],
                authenticity=question_data['authenticity'],
                explanation=question_data['explanation'],
                # ... other fields
            )
            question.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully imported question: {question.summary}'))
