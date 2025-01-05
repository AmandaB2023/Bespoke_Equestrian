from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings 
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Contact
import os


"""view to create and send contact query"""


def contact_view(request):
    admin_email = os.environ.get("EMAIL_ADMIN_ADDRESS")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                form.cleaned_data['subject'],  # subject
                f" ou have recieved a Message from {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['message']}",  # message
                None,  # from email
                ['admin_email'],  # replace with your email
            )
        return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def contact_success(request):
    return render(request, 'contact/success.html')
