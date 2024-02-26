from django.urls import path
from .views import cleaner_dashboard

app_name = 'bookings'

urlpatterns = [
    path('dashboard/', cleaner_dashboard, name='cleaner_dashboard'),

]