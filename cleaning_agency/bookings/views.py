from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CleanerAvailability, TimeSlot
from .forms import CleanerAvailabilityForm
from datetime import datetime, timedelta

@login_required
def cleaner_dashboard(request):
    if not request.user.is_cleaner:
        return redirect('home')

    # Generate dates for the next two months
    today = datetime.today()
    future = today + timedelta(days=60)
    date_list = [today + timedelta(days=x) for x in range((future-today).days + 1)]

    # Get or create availability instances for each date
    availability_list = [CleanerAvailability.objects.get_or_create(cleaner=request.user, date=date)[0] for date in date_list]
    
    # Create a form for each availability instance
    forms = [CleanerAvailabilityForm(instance=availability, prefix=str(availability.date)) for availability in availability_list]
    
    # Handle form submission
    if request.method == 'POST':
        # Update each availability instance with the submitted timeslots
        for form in forms:
            if form.is_valid():
                form.save()
        return redirect('cleaner_dashboard')

    # Pass the forms and the date list to the template
    context = {
        'forms': zip(date_list, forms),
    }
    return render(request, 'bookings/cleaner_dashboard.html', context)