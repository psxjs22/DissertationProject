from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class TreatmentGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ConsentForm(models.Model):
    id = models.AutoField(primary_key=True)
    initials = models.CharField(max_length=10)
    date = models.DateField(default='2023-01-01')
    signed = models.BooleanField()

    def __str__(self):
        return f"ConsentForm ID: {self.id}, Initials: {self.initials}, Confirmed: {self.signed}"

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    consent_form = models.ForeignKey(ConsentForm, on_delete=models.CASCADE, related_name='participants')
    treatment_group = models.ForeignKey(TreatmentGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Participant ID: {self.id}, ConsentForm ID: {self.consent_form.id}"


class Demographic(models.Model):
    id = models.AutoField(primary_key=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    def __str__(self):
        return f"Demographics for Participant ID: {self.participant_id}"


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    summary = models.TextField()
    image = models.CharField(max_length=255)
    details = models.TextField()
    link = models.TextField()
    authenticity = models.CharField(max_length=10)
    explanation = models.TextField()

    def __str__(self):
        return self.summary


class Response(models.Model):
    id = models.AutoField(primary_key=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=10)  # 'Real' or 'Fake'
    confidence = models.PositiveIntegerField()  # 1 to 5
    reason = models.TextField()
    attempt = models.PositiveIntegerField()  # 1 for first attempt, 2 for second

    def __str__(self):
        return f"Response for Participant: {self.participant}, Question: {self.question}, Response: {self.response}"





