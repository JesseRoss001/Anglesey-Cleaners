# forms.py
from django import forms
from .models import CleanerAvailability, TimeSlot

class CleanerAvailabilityForm(forms.ModelForm):
    timeslot = forms.ModelMultipleChoiceField(
        queryset=TimeSlot.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = CleanerAvailability
        fields = ['date', 'timeslot']