from django.urls import path
from .views import cleaner_dashboard, update_rates

urlpatterns = [
    path('dashboard/', cleaner_dashboard, name='cleaner_dashboard'),
    path('update_rates/', update_rates, name='update_rates'),
]