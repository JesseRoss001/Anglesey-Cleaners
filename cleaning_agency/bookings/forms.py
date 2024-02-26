from django import forms
from django.contrib.auth import get_user_model
from .models import CleanerAvailability

User = get_user_model()

class UpdateRatesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['hourly_rate']

class CleanerAvailabilityForm(forms.ModelForm):
    class Meta:
        model = CleanerAvailability
        fields = ['date', 'start_time', 'end_time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }