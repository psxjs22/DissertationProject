from django.db import models
from django.utils import timezone

class TreatmentGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ConsentForm(models.Model):
    initials = models.CharField(max_length=10)
    date = models.DateField(default=timezone.now)
    signed = models.BooleanField()

    def __str__(self):
        return f"ConsentForm ID: {self.id}, Initials: {self.initials}, Confirmed: {self.signed}"

class Participant(models.Model):
    consent_form = models.ForeignKey(ConsentForm, on_delete=models.CASCADE, related_name='participants')
    treatment_group = models.ForeignKey(TreatmentGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Participant ID: {self.id}, ConsentForm ID: {self.consent_form.id}"

class Demographic(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    def __str__(self):
        return f"Demographics for Participant ID: {self.participant_id}"

class Question(models.Model):
    summary = models.TextField()
    image = models.CharField(max_length=255)
    details = models.TextField()
    link = models.TextField()
    authenticity = models.CharField(max_length=10)
    explanation = models.TextField()

    def __str__(self):
        return self.summary

class Response(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=10)  # 'Real' or 'Fake'
    confidence = models.PositiveIntegerField()  # 1 to 5
    reason = models.TextField()
    attempt = models.PositiveIntegerField()  # 1 for first attempt, 2 for second

    def __str__(self):
        return f"Response for Participant: {self.participant}, Question: {self.question}, Response: {self.response}"


class Tutorial(models.Model):
    page_title = models.CharField(max_length=255)
    video_url = models.URLField()
    intro_text = models.TextField()

    def __str__(self):
        return self.page_title


class UsabilityQuestionnaire(models.Model):
    # Questions for evaluating content, organisation, and readability
    easy_to_find = models.PositiveIntegerField()
    well_organised = models.PositiveIntegerField()
    easy_to_read = models.PositiveIntegerField()
    comfortable_language = models.PositiveIntegerField()
    no_left_right_scroll = models.PositiveIntegerField()

    # Questions for evaluating navigation and links
    know_where_i_am = models.PositiveIntegerField()
    useful_cues_links = models.PositiveIntegerField()
    easy_to_move_around = models.PositiveIntegerField()
    well_maintained_links = models.PositiveIntegerField()
    not_many_new_windows = models.PositiveIntegerField()
    standard_placement_links = models.PositiveIntegerField()

    # Questions for evaluating user interface design
    attractive_design = models.PositiveIntegerField()
    comfortable_colors = models.PositiveIntegerField()
    no_irritating_features = models.PositiveIntegerField()
    consistent_look = models.PositiveIntegerField()
    easy_to_learn = models.PositiveIntegerField()

    # Questions for evaluating performance and effectiveness
    fast_downloads = models.PositiveIntegerField()
    distinguish_links = models.PositiveIntegerField()
    expected_responses = models.PositiveIntegerField()
    efficient_use = models.PositiveIntegerField()
    clear_useful_messages = models.PositiveIntegerField()

    # Other fields (participant, timestamp, etc.) can be added here

    def __str__(self):
        return f"Usability Questionnaire - Participant {self.id}"