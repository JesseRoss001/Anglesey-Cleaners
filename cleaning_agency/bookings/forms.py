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
        widgets = {'date': forms.HiddenInput()}  # Set the date field as a hidden input