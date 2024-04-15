# contact/views.py
from django.shortcuts import render

def contact_page(request):
    return render(request, 'contact/contact.html')