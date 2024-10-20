from django.contrib import admin
from .models import Faq
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Faq)
class FaqAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)