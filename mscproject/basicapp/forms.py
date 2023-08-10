from django import forms
from .models import ConsentForm, Participant


class ConsentFormForm(forms.ModelForm):
    class Meta:
        model = ConsentForm
        # Exclude the 'participant' field from the form
        exclude = ['participant']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
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

    gender = forms.ChoiceField(choices=gender_choices)
    age = forms.ChoiceField(choices=age_choices)
    ethnicity = forms.ChoiceField(choices=ethnicity_choices)
    occupation = forms.ChoiceField(choices=occupation_choices)
    education = forms.ChoiceField(choices=education_choices)