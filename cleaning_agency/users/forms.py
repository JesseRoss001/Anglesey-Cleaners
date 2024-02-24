from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User, GeneralLocation

class CustomerSignUpForm(UserCreationForm):
    postcode = forms.CharField(max_length=10)
    address_line_1 = forms.CharField(max_length=100)
    address_line_2 = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=50)
    selected_areas = forms.ModelMultipleChoiceField(queryset=GeneralLocation.objects.all())


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'postcode', 'address_line_1', 'address_line_2', 'city', 'selected_areas')

class CleanerSignUpForm(UserCreationForm):
    contact_number = forms.CharField(max_length=20)
    hourly_rate = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField(required=False)
    general_area = forms.ModelChoiceField(queryset=GeneralLocation.objects.all(), required=False)
    selected_areas = forms.ModelMultipleChoiceField(
        queryset=GeneralLocation.objects.all(),
        required=False,
        help_text="Tap to select multiple areas. On desktop, hold down the Ctrl (windows) / Command (Mac) button to select multiple options."
    )


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'contact_number', 'hourly_rate', 'image', 'general_area', 'selected_areas')