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


GENDER_LIST = (['1', 'Male'], ['2', 'Female'], ['3', 'Non-Binary'], ['4', 'Other'], ['5', 'Prefer not to say'])

AGE_LIST = (['1', '18-24'], ['2', '25-29'], ['3', '30-34'],
            ['4', '35-39'], ['5', '40-44'], ['6', '45-49'],
            ['7', '50-54'], ['8', '55-59'], ['9', '60-64'],
            ['10', '65-69'], ['11', '70-74'], ['12', '75-79'],
            ['13', '80-84'], ['14', 'Age 85 and over'])

ETHNICITY_LIST = (('Asian or Asian British',
                   (('1', 'Indian'),
                    ('2', 'Pakistani'),
                    ('3', 'Bangladeshi'),
                    ('4', 'Chinese'),
                    ('5', 'Any other Asian background'))),
                ('Black or Black British',
                   (('1', 'Caribbean'),
                    ('2', 'African'),
                    ('3', 'Any other Black, Black British or Caribbean background'))),
                ('Mixed or multiple ethnic groups',
                   (('1', 'White and Black Caribbean'),
                    ('2', 'White and Black African'),
                    ('3', 'White and Asian'),
                    ('4', 'Any other Mixed or multiple ethnic background'))),
                ('White',
                   (('1', 'English, Welsh, Scottish, Northern Irish or British'),
                    ('2', 'Irish'),
                    ('3', 'Gypsy or Irish Traveller'),
                    ('4', 'Roma'),
                    ('5', 'Any other White background'))),
                ('Other ethnic group',
                   (('1', 'Arab'),
                    ('2', 'Any other ethnic group'))))

OCCUPATION_LIST = (['1', 'Managers, Directors and Senior Officials'],
                   ['2', 'Professional Occupations'],
                   ['3', 'Associate Professional and Technical Occupations'],
                   ['4', 'Administrative and Secretarial Occupations'],
                   ['5', 'Skilled Trades Occupations'],
                   ['6', 'Caring, Leisure and Other Service Occupations'],
                   ['7', 'Sales and Customer Service Occupations'],
                   ['8', 'Process, Plant and Machine Operatives'],
                   ['9', 'Elementary Occupations'],
                   ['10', 'Retired'],
                   ['11', 'Full Time Student'],
                   ['12', 'Not in Employment'],
                   ['13', 'Other'])


EDUCATION_LIST = (['1', 'Primary School'],
                  ['2', 'Secondary School'],
                  ['3', 'Higher or secondary or further education (A-levels, BTEC, professional certificate.)'],
                  ['4', 'University, of equivalent'],
                  ['5', 'Post-graduate degree'],
                  ['6', 'Other'],
                  ['7', 'Prefer not to say'])


class Demographic(models.Model):

    gender_choices = list(GENDER_LIST)
    age_choices = list(AGE_LIST)
    ethnicity_choices = list(ETHNICITY_LIST)
    occupation_choices = list(OCCUPATION_LIST)
    education_choices = list(EDUCATION_LIST)

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=gender_choices)
    age = models.IntegerField(choices=age_choices)
    ethnicity = models.CharField(max_length=50, choices=ethnicity_choices)
    occupation = models.CharField(max_length=100, choices=occupation_choices)
    education = models.CharField(max_length=100, choices=education_choices)

    def __str__(self):
        return f"Demographics for Participant ID: {self.participant_id}, Gender: {self.get_gender_display()}, Age: {self.get_age_display()}, Ethnicity: {self.get_ethnicity_display()}, Occupation: {self.get_occupation_display()}, Education: {self.get_education_display()}"


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