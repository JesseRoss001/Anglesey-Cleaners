from django import forms
from .models import User, CleanerAvailability

class UpdateRatesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['hourly_rate']
        widgets = {
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CleanerAvailabilityForm(forms.ModelForm):
    class Meta:
        model = CleanerAvailability
        fields = ['date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }