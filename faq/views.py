from django.shortcuts import render
from .models import Faq


def faq_app(request):
    """
    Renders the Faq page
    """
    faq = Faq.objects.all().last()

    return render(
        request,
        "faq/faq.html",
        {"faq": faq},
    )