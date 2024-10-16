from django.contrib import admin
from .models import Contact


class Contact_View(admin.ModelAdmin):
# Tells admin what headings to display
    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )