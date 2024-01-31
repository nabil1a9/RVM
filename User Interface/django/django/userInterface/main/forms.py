from django import forms
from .models import Note, RATE_CHOICES

class RateForm (forms.Form):
    rate = forms.ChoiceField (choices=RATE_CHOICES, widget=forms.Select())