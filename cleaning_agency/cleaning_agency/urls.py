from django.contrib import admin
from django.urls import path, include
from users.views import home  # Import the home view directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Set the home view at the root URL
    path('users/', include('users.urls')),  # Keep other users URLs
    path('bookings/', include('bookings.urls')),  # Include your bookings.urls
]