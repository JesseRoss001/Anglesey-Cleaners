from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from bookings.models import GeneralLocation

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_cleaner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    approved = models.BooleanField(default=False)  
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  
    image = models.ImageField(upload_to='cleaner_images/', null=True, blank=True)  
    # Add related_name for general_area and selected_areas to avoid clashing



class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_profile")
    selected_areas = models.ManyToManyField(GeneralLocation, verbose_name="Selected Service Areas") 
    postcode = models.CharField(max_length=10)  
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s profile - Areas: {', '.join(area.name for area in self.selected_areas.all())}"