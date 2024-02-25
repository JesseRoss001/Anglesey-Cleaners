from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateRatesForm, CleanerAvailabilityForm
from .models import CleanerAvailability

@login_required
def cleaner_dashboard(request):
    if not request.user.is_cleaner:
        return redirect('home')  # Redirect non-cleaners
    availability_form_set = modelformset_factory(CleanerAvailability, form=CleanerAvailabilityForm, extra=1)
    if request.method == 'POST':
        formset = availability_form_set(request.POST, queryset=CleanerAvailability.objects.filter(cleaner=request.user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.cleaner = request.user
                instance.save()
            return redirect('cleaner_dashboard')
    else:
        formset = availability_form_set(queryset=CleanerAvailability.objects.filter(cleaner=request.user))
    rate_form = UpdateRatesForm(instance=request.user)
    return render(request, 'cleaners/cleaner_dashboard.html', {
        'rate_form': rate_form,
        'formset': formset,
    })

@login_required
def update_rates(request):
    if request.method == 'POST':
        form = UpdateRatesForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('cleaner_dashboard')
    else:
        form = UpdateRatesForm(instance=request.user)
    return render(request, 'update_rates.html', {'form': form})