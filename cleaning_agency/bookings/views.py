# bookings/views.py
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .forms import CleanerAvailabilityForm
from .models import CleanerAvailability, TimeSlot

def availability_dashboard(request):
    today = datetime.now().date()
    days = [today + timedelta(days=i) for i in range(7)]
    days_forms = []

    for day in days:
        availability, created = CleanerAvailability.objects.get_or_create(
            cleaner=request.user,
            date=day,
        )
        form = CleanerAvailabilityForm(instance=availability)
        days_forms.append((day, form))

    context = {
        'days_forms': days_forms,
    }
    return render(request, 'bookings/availability_dashboard.html', context)
def update_availability(request, date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    availability, created = CleanerAvailability.objects.get_or_create(
        cleaner=request.user, 
        date=date_obj,
    )

    if request.method == 'POST':
        form = CleanerAvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            # Redirect back to the dashboard to show the saved state
            return redirect('availability_dashboard')
        else:
            # If form is not valid, re-render the dashboard with the form errors
            days_forms = [(date_obj, form)] + [(day, CleanerAvailabilityForm(instance=avail)) for day, avail in days_forms if day != date_obj]
            return render(request, 'bookings/availability_dashboard.html', {'days_forms': days_forms})

    # If not POST, redirect to the dashboard
    return redirect('availability_dashboard')


def update_availability(request, date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    availability, _ = CleanerAvailability.objects.get_or_create(
        cleaner=request.user, 
        date=date_obj
    )

    if request.method == 'POST':
        form = CleanerAvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            return redirect('availability_dashboard')  # Redirect back to the dashboard
        else:
            # If the form is not valid, you can show the form with errors
            # You might need to pass all forms and dates back to the template if you want to show the dashboard
            # For now, just redirect to the dashboard
            return redirect('availability_dashboard')