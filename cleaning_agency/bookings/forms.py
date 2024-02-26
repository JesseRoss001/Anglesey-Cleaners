from django import forms
from .models import CleanerAvailability, TimeSlot
from django.contrib.auth import get_user_model

class CleanerAvailabilityForm(forms.ModelForm):
    timeslot = forms.ModelMultipleChoiceField(
        queryset=TimeSlot.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = CleanerAvailability
        fields = ['date', 'timeslot', 'notes']
        widgets = {
            'date': forms.HiddenInput(),  # The date will be auto-filled, hence hidden
            'notes': forms.Textarea(attrs={'rows': 2}),
        }