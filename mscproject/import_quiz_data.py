import json
from django.core.management.base import BaseCommand
from myapp.models import QuizItem, Option


class Command(BaseCommand):
    help = 'Import quiz data from JSON file'

    def handle(self, *args, **options):
        with open('quiz_data.json', 'r') as json_file:
            quiz_data = json.load(json_file)

        for item_data in quiz_data:
            quiz_item = QuizItem.objects.create(
                summary=item_data['summary'],
                image=item_data['image'],
                details=item_data['details'],
                authenticity=item_data['authenticity'],
                explanation=item_data['explanation']
            )

            for option_data in item_data['options']:
                Option.objects.create(
                    quiz_item=quiz_item,
                    text=option_data['text'],
                    correct=option_data['correct']
                )

        self.stdout.write(self.style.SUCCESS('Quiz data imported successfully'))
