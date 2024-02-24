#users urls
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # For built-in login/logout

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('signup/customer/', views.customer_signup, name='customer_signup'),
    path('signup/cleaner/', views.cleaner_signup, name='cleaner_signup'),  # Define the path for the home view
    path('book-now/', views.book_now, name='book_now'),  # Add the book now view
    path('logout/', views.logout_request, name='logout'),  # Add the logout view
]