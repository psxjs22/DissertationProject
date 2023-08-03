from django.db import models


class TreatmentGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ConsentForm(models.Model):
    initials = models.CharField(max_length=3)
    date = models.DateField(default='2023-01-01')
    signed = models.BooleanField()

    def __str__(self):
        return f"ConsentForm ID: {self.id}, Initials: {self.initials}, Confirmed: {self.signed}"


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    consent_form = models.ForeignKey(ConsentForm, on_delete=models.CASCADE, related_name='participants')
    treatment_group = models.ForeignKey(TreatmentGroup, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Participant ID: {self.id}, ConsentForm ID: {self.consent_form.id}"


class Demographics(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    def __str__(self):
        return f"Demographics for Participant ID: {self.participant_id}"


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    claim = models.TextField()
    source = models.CharField(max_length=100)
    image = models.CharField(max_length=200)  # Use CharField for a short line of text as the image URL

    def __str__(self):
        return f"Question ID: {self.id}, Quiz: {self.quiz}, Claim: {self.claim}"


class Answers(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key=True)
    authenticity = models.CharField(max_length=100)
    explanation = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return f"Answers for Question ID: {self.question_id}"


class Responses(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)
    reason = models.TextField()
    result = models.CharField(max_length=100)

    def __str__(self):
        return f"Response ID: {self.id}, Participant: {self.participant}, Question: {self.question}, Response: {self.response}"
