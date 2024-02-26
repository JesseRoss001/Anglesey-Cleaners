from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from datetime import datetime, timedelta
from .models import CleanerAvailability
from .forms import CleanerAvailabilityForm

@login_required
def cleaner_dashboard(request):
    if not request.user.is_cleaner:
        return redirect('home')

    # Generate dates for the next two months
    today = datetime.today()
    future = today + timedelta(days=60)
    date_list = [today + timedelta(days=x) for x in range((future-today).days + 1)]

    if request.method == 'POST':
        for date in date_list:
            form = CleanerAvailabilityForm(request.POST, prefix=str(date))
            if form.is_valid():
                availability = form.save(commit=False)
                availability.cleaner = request.user
                availability.date = date
                availability.save()
        return redirect('cleaner_dashboard')
    else:
        forms = {date: CleanerAvailabilityForm(prefix=str(date)) for date in date_list}

    context = {
        'forms': forms,
    }
    return render(request, 'bookings/cleaner_dashboard.html', context)