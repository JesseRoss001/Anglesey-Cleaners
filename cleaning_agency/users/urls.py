#users urls
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Define the path for the home view
]