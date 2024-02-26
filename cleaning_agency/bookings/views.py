from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import UpdateRatesForm, CleanerAvailabilityForm
from .models import CleanerAvailability
from django.utils.dateparse import parse_datetime
import json
@login_required
def cleaner_dashboard(request):
    if not request.user.is_cleaner:
        return redirect('home')

    # Updating rates
    rate_form = UpdateRatesForm(request.POST or None, instance=request.user)
    if request.method == 'POST' and 'update_rates' in request.POST:
        if rate_form.is_valid():
            rate_form.save()

    # Handling availability formset
    AvailabilityFormSet = modelformset_factory(CleanerAvailability, form=CleanerAvailabilityForm, extra=1)
    formset = AvailabilityFormSet(request.POST or None, queryset=CleanerAvailability.objects.filter(cleaner=request.user), prefix='availabilities')

    if request.method == 'POST' and 'update_availability' in request.POST:
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.cleaner = request.user
                instance.save()
            formset.save_m2m()
            return redirect('bookings:cleaner_dashboard')

    # Check for an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        availabilities = CleanerAvailability.objects.filter(cleaner=request.user)
        events = [
            {
                'title': f"Available ({availability.notes})" if availability.notes else "Available",
                'start': f"{availability.date.isoformat()}T{availability.start_time.isoformat()}",
                'end': f"{availability.date.isoformat()}T{availability.end_time.isoformat()}",
            }
            for availability in availabilities
        ]
        return JsonResponse(events, safe=False)

    context = {
        'rate_form': rate_form,
        'formset': formset,
    }

    return render(request, 'bookings/cleaner_dashboard.html', context)


@login_required
def get_events(request):
    if not request.user.is_cleaner:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    # You might want to filter these by date range passed in the request
    availabilities = CleanerAvailability.objects.filter(cleaner=request.user)
    
    events = [
        {
            'id': availability.id,
            'title': availability.notes if availability.notes else "Available",
            'start': f"{availability.date.isoformat()}T{availability.start_time.isoformat()}",
            'end': f"{availability.date.isoformat()}T{availability.end_time.isoformat()}",
            'editable': True,  # If you want to allow drag and drop in the calendar
        }
        for availability in availabilities
    ]
    
    return JsonResponse(events, safe=False)