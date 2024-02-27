# bookings/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime, timedelta
from .forms import CleanerAvailabilityForm
from .models import CleanerAvailability

def availability_dashboard(request):
    # Retrieve the 'week' parameter, and use a default of 0 if it's not provided or empty
    week_param = request.GET.get('week') or '0'
    try:
        week_offset = int(week_param)
    except ValueError:
        week_offset = 0  # Default to the current week if the conversion fails

    # Calculate the start and end dates for the current week's view based on the week offset
    start_date = datetime.now().date() + timedelta(weeks=week_offset)
    end_date = start_date + timedelta(days=7)

    # Generate the dates and forms for the week
    days_forms = []
    for single_date in (start_date + timedelta(days=n) for n in range(7)):
        availability, created = CleanerAvailability.objects.get_or_create(
            cleaner=request.user, 
            date=single_date
        )
        form = CleanerAvailabilityForm(instance=availability, prefix=str(single_date))
        days_forms.append((single_date, form))

    # Pass the current week offset, and calculate the previous and next week offsets
    previous_week_offset = week_offset - 1 if week_offset > 0 else None
    next_week_offset = week_offset + 1

    return render(request, 'bookings/availability_dashboard.html', {
        'days_forms': days_forms,
        'previous_week_offset': previous_week_offset,
        'next_week_offset': next_week_offset,
    })

def update_availability(request, date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    availability, created = CleanerAvailability.objects.get_or_create(
        cleaner=request.user, 
        date=date_obj
    )

    if request.method == 'POST':
        form = CleanerAvailabilityForm(request.POST, instance=availability, prefix=str(date_obj))
        if form.is_valid():
            form.save()
            # Calculate the week offset based on the date saved
            current_date = datetime.now().date()
            week_offset = (date_obj - current_date).days // 7
            return redirect(reverse('availability_dashboard') + f'?week={week_offset}')
        else:
            # If the form is not valid, include logic to handle errors
            pass

    # If it's not a POST request or if the form is invalid, redirect back to the dashboard
    current_date = datetime.now().date()
    week_offset = (date_obj - current_date).days // 7
    return redirect(reverse('availability_dashboard') + f'?week={week_offset}')
