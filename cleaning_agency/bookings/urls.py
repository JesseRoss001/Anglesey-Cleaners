from django.urls import path
from .views import cleaner_dashboard, get_events 

app_name = 'bookings'

urlpatterns = [
    path('dashboard/', cleaner_dashboard, name='cleaner_dashboard'),
     path('your-endpoint-to-get-events/', get_events, name='get_events'),
]