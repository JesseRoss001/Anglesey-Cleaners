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
        fields = ['date', 'start_time', 'end_time', 'notes']  # Include the new 'notes' field
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),  # Widget for notes
        }