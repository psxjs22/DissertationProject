from django.db import models


class TreatmentGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)


class ConsentForm(models.Model):
    initials = models.CharField(max_length=3)
    confirmed = models.BooleanField(default=False)


class Participant(models.Model):
    treatment_group = models.ForeignKey(TreatmentGroup, on_delete=models.CASCADE)
    consent_form = models.ForeignKey(ConsentForm, on_delete=models.CASCADE)


class Demographics(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    education = models.CharField(max_length=100)


class Quiz(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    claim = models.TextField()
    source = models.CharField(max_length=100)
    image = models.TextFieldg(null=True)


class Answers(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key=True)
    authenticity = models.CharField(max_length=100)
    explanation = models.TextField()
    url = models.URLField()


class Response(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField()
    reason = models.TextField()
    result = models.BooleanField()
