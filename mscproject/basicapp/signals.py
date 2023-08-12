from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from .models import TreatmentGroup, Question


#Remember to update ConsentCreate in views.py with number of treatment groups to ensure they get assigned correctly
def populate_treatment_groups(sender, **kwargs):
    if sender.name == 'basicapp':
        TreatmentGroup.objects.get_or_create(
            name='Control',
            description='Control group, no gamified solution'
        )
        TreatmentGroup.objects.get_or_create(
            name='GS1',
            description='Gamified solution 1, using xxx'
        )
        TreatmentGroup.objects.get_or_create(
            name='GS2',
            description='Gamified solution 2, using xxx'
        )


def trigger_populate_treatment_groups(sender, **kwargs):
    if sender.name == 'basicapp':
        populate_treatment_groups(sender, **kwargs)


@receiver(post_migrate)
def populate_questions(sender, **kwargs):
    if sender.name == 'basicapp':
        from django.core.management import call_command
        call_command('loaddata', 'basicapp/fixtures/quiz.json')
