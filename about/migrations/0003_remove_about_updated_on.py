# Generated by Django 5.1.1 on 2024-10-17 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_profile_image_alter_about_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='updated_on',
        ),
    ]