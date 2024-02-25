from django.db import models
from django.conf import settings

class GeneralLocation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CleanerAvailability(models.Model):
    cleaner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="available_times")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.cleaner.username} available on {self.date} from {self.start_time} to {self.end_time}"


class Booking(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_bookings")
    cleaner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cleaner_bookings")
    location = models.ForeignKey(GeneralLocation, on_delete=models.CASCADE, verbose_name="Service Location")
    booking_date = models.DateTimeField()
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')])
    payment_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Refunded', 'Refunded')])
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return f"Booking at {self.location.name} by {self.customer.username} with {self.cleaner.username} on {self.booking_date}"

class Rating(models.Model):
    cleaner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ratings', on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rated_by', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cleaner', 'customer')

    def __str__(self):
        return f"Rating for {self.cleaner.username} by {self.customer.username}: {self.score} stars"
# Create your models here.
