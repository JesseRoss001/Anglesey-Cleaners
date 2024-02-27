# bookings/urls.py
from django.urls import path
from .views import availability_dashboard , update_availability

urlpatterns = [
    # ... other URL patterns ...
    path('dashboard/', availability_dashboard, name='availability_dashboard'),
    path('update_availability/<str:date_str>/', update_availability, name='update_availability'),
]