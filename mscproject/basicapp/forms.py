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

