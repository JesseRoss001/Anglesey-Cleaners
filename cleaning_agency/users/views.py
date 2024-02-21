from django.shortcuts import render

def home(request):
    # Your logic for the home page can go here
    return render(request, 'users/home.html')  # Render the home page template