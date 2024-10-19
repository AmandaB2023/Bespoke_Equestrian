from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact

"""view to create and send contact query"""
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],  # subject
                f"Message from {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['message']}",  # message
                None,  # from email
                ['bespokeequestrian@example.com'],  # replace with your email
            )
            return render(request, 'contact/success.html', context)  
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)   


def contact_success(request):
    return render(request, 'contact/success.html')