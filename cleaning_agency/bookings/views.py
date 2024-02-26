from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CleanerAvailability, TimeSlot
from .forms import CleanerAvailabilityForm
from datetime import datetime, timedelta

@login_required
def cleaner_dashboard(request):
    today = timezone.localdate()
    start_of_week = today - timedelta(days=today.weekday())
    week_param = request.GET.get('week')

    if week_param:
        try:
            start_of_week = datetime.strptime(week_param, '%Y-%m-%d').date()
        except ValueError:
            pass  # If the parameter is invalid, the default start of the week is used

    end_week = start_of_week + timedelta(days=6)
    date_list = [start_of_week + timedelta(days=x) for x in range(7)]

    if request.method == 'POST':
        form = CleanerAvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.cleaner = request.user
            availability.save()
            form.save_m2m()  # Since we used commit=False earlier, we need to save many-to-many fields manually
            # Respond with JSON data
            return JsonResponse({'success': True, 'date': availability.date.strftime('%Y-%m-%d'), 'timeslots': list(availability.timeslot.values_list('id', flat=True))})
        else:
            # Log form errors to the console.
            print(form.errors)
            return JsonResponse({'success': False, 'errors': form.errors.get_json_data()})

    # Prepare forms for each day of the week
    availability_list = [CleanerAvailability.objects.get_or_create(cleaner=request.user, date=date)[0] for date in date_list]
    forms = [CleanerAvailabilityForm(initial={'date': date}, instance=availability, prefix=str(availability.date)) for date, availability in zip(date_list, availability_list)]

    context = {
        'forms': zip(date_list, forms),
        'next_week': (end_week + timedelta(days=1)).strftime('%Y-%m-%d'),
        'prev_week': (start_of_week - timedelta(days=7)).strftime('%Y-%m-%d'),
        'current_week': start_of_week.strftime('%Y-%m-%d'),
    }

    return render(request, 'bookings/cleaner_dashboard.html', context)