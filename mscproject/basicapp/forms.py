from django import forms
from .models import ConsentForm, Participant, Demographic, Response, UsabilityQuestionnaire
from django.utils import timezone


class ConsentFormForm(forms.ModelForm):
    signed = forms.BooleanField(
        required=True,
        label="I agree that I have read and understood the above information and am happy to proceed.",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = ConsentForm
        exclude = ['participant']
        widgets = {
            'initials': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': timezone.now().date().isoformat()})
        }


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


class DemographicsForm(forms.Form):
    placeholder = [('', 'Select an option from the dropdown')]
    gender_choices = placeholder + list(GENDER_LIST)
    age_choices = placeholder + list(AGE_LIST)
    ethnicity_choices = placeholder + list(ETHNICITY_LIST)
    occupation_choices = placeholder + list(OCCUPATION_LIST)
    education_choices = placeholder + list(EDUCATION_LIST)

    gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select(attrs={'class': 'text-center'}))
    age = forms.ChoiceField(choices=age_choices, widget=forms.Select(attrs={'class': 'text-center'}))
    ethnicity = forms.ChoiceField(choices=ethnicity_choices, widget=forms.Select(attrs={'class': 'text-center'}))
    occupation = forms.ChoiceField(choices=occupation_choices, widget=forms.Select(attrs={'class': 'text-center'}))
    education = forms.ChoiceField(choices=education_choices, widget=forms.Select(attrs={'class': 'text-center'}))


class QuizResponseForm(forms.Form):
    RESPONSE_CHOICES = [
        ('real', 'Real'),
        ('fake', 'Fake'),
    ]

    CONFIDENCE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    response = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'role': 'switch'}),
        label='Do you think the article was more likely to be real or fake?'
    )
    confidence = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 1, 'max': 5, 'step': 1}),
        label='How confident do you feel about your choice (1 = Not confident, 5 = Very confident)?'
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        label='Provide a brief reason for your choice (optional).',
        required=False
    )

    class Meta:
        model = Response
        fields = ['response', 'confidence', 'reason']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.widgets.NumberInput):
                field.widget = forms.widgets.TextInput(
                    attrs={'type': 'range', 'min': '1', 'max': '5', 'class': 'form-control-slider', 'step': 1})


class UsabilityQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = UsabilityQuestionnaire
        fields = '__all__'
        labels = {
            # Questions for evaluating content, organisation, and readability

            'easy_to_find': 'I can easily find what I want at this website.',
            'well_organised': 'The content of this website is well organised.',
            'easy_to_read': 'Reading content at this website is easy.',
            'comfortable_language': 'I am comfortable and familiar with the language used.',
            'no_left_right_scroll': 'I need not scroll left and right when reading at this website.',

            # Questions for evaluating navigation and links
            'know_where_i_am': 'I can easily know where I am at this website.',
            'useful_cues_links': 'This website provides useful cues and links for me to get the desired information.',
            'easy_to_move_around': 'It is easy to move around at this website by using the links or back button of the browser.',
            'well_maintained_links': 'The links at this website are well maintained and updated.',
            'not_many_new_windows': 'The website does not open too many new browser windows when I am moving around.',
            'standard_placement_links': 'Placement of links or menu is standard throughout the website and I can easily recognise them.',

            # Questions for evaluating user interface design
            'attractive_design': "This website’s interface design is attractive.",
            'comfortable_colors': "I am comfortable with the colours used at this website.",
            'no_irritating_features': "This website contains no feature that irritates me such as scrolling or blinking text and looping animations.",
            'consistent_look': "This website has a consistent feel and look.",
            'easy_to_learn': "The design of the website makes sense and it is easy to learn how to use it.",

            # Questions for evaluating performance and effectiveness
            'fast_downloads': "I need not wait too long to download a file or open a page.",
            'distinguish_links': "I can easily distinguish between visited and not-visited links.",
            'expected_responses': "This website responds to my actions as expected.",
            'efficient_use': "It is efficient to use this website.",
            'clear_useful_messages': "This website always provides clear and useful messages when I don’t know how to proceed.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add sliders for rating questions
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.widgets.NumberInput):
                field.widget = forms.widgets.TextInput(attrs={'type': 'range', 'min': '1', 'max': '5'})