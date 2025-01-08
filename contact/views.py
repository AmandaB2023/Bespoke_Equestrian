from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings 
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Contact
import os


"""view to create and send contact query"""


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
        return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def contact_success(request):
    return render(request, 'contact/success.html')
