from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_cleaner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    approved = models.BooleanField(default=False)  # For cleaner approval by admin
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Optional: For cleaners
    image = models.ImageField(upload_to='cleaner_images/', null=True, blank=True)  # Optional: For cleaners

class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_profile")
    selected_area = models.ForeignKey('bookings.GeneralLocation', on_delete=models.CASCADE, verbose_name="Selected Service Area")

    def __str__(self):
        return f"{self.user.username}'s profile - Area: {self.selected_area.name}"
# Create your models here.
