# contact/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send the email
            send_mail(
                f"Message from {form.cleaned_data['name']}", 
                form.cleaned_data['message'],
                settings.DEFAULT_FROM_EMAIL, 
                ['help.angleseycleaners@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({"message": "Email sent successfully."}, status=200)
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
