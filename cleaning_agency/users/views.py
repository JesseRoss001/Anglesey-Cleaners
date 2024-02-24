from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import CustomerSignUpForm, CleanerSignUpForm 
from .models import CustomerProfile # You might create a CleanerProfile model similarly
from django.contrib.auth.decorators import login_required
from bookings.models import GeneralLocation
def home(request):
    # Your logic for the home page can go here
    return render(request, 'users/home.html')  # Render the home page template


def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            
            # Assuming 'selected_areas' returns a list of IDs for GeneralLocation instances
            selected_area_ids = form.cleaned_data['selected_areas']
            selected_areas = GeneralLocation.objects.filter(id__in=selected_area_ids)

            # Create CustomerProfile
            customer_profile = CustomerProfile.objects.create(
                user=user,
                postcode=form.cleaned_data['postcode'],
                address_line_1=form.cleaned_data['address_line_1'],
                address_line_2=form.cleaned_data.get('address_line_2', ''),
                city=form.cleaned_data['city']
            )
            
            # Assign selected_areas
            customer_profile.selected_areas.set(selected_areas)
            
            login(request, user)
            return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'users/customer_signup.html', {'form': form})


def cleaner_signup(request):
    if request.method == 'POST':
        form = CleanerSignUpForm(request.POST, request.FILES) 
        if form.is_valid():
            user = form.save(commit=False)  # Don't save just yet
            user.is_cleaner = True

            # Set cleaner-specific fields
            user.contact_number = form.cleaned_data['contact_number'] 
            user.hourly_rate = form.cleaned_data['hourly_rate']
            user.general_area = form.cleaned_data['general_area']

            user.save()  # Now save the user

            # Image Handling 
            if form.cleaned_data.get('image'): 
                user.image = form.cleaned_data['image']
                user.save()  # Save again if the image was updated

            # Many-to-Many Relationship
            user.selected_areas.set(form.cleaned_data['selected_areas']) 

            # You likely don't need to create a CleanerProfile here since
            # the cleaner-specific data is already on the User model

            login(request, user)
            return redirect('home')  
    else:
        form = CleanerSignUpForm()
    return render(request, 'users/cleaner_signup.html', {'form': form})

@login_required
def book_now(request):
    # Your logic for booking a service can go here
    return render(request, 'users/book_now.html')  # Render the book now page template

def logout_request(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout