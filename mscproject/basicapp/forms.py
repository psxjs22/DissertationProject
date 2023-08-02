from django import forms
from .models import ConsentForm


class ConsentFormForm(forms.ModelForm):
    class Meta:
        model = ConsentForm
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})}

