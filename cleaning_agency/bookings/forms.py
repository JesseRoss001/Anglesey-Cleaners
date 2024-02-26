from django import forms
from .models import CleanerAvailability, TimeSlot

class CleanerAvailabilityForm(forms.ModelForm):
    timeslot = forms.ModelMultipleChoiceField(
        queryset=TimeSlot.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    date = forms.DateField(widget=forms.HiddenInput())  # Explicitly define the date field

    class Meta:
        model = CleanerAvailability
        fields = ['date', 'timeslot', 'notes']

    def __init__(self, *args, **kwargs):
        super(CleanerAvailabilityForm, self).__init__(*args, **kwargs)
        # Set the initial value for the date field if it's not already set
        if 'initial' in kwargs and 'date' in kwargs['initial']:
            self.fields['date'].initial = kwargs['initial']['date']