#users urls
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # For built-in login/logout

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('signup/customer/', views.customer_signup, name='customer_signup'),
    path('signup/cleaner/', views.cleaner_signup, name='cleaner_signup'),  # Define the path for the home view
    path('book-now/', views.book_now, name='book_now'),  # Add the book now view
    path('logout/', views.logout_request, name='logout'), 
    path('login/', views.login_request, name='login'), # Add the logout view
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]