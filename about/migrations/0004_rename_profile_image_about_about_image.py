# Generated by Django 5.1.1 on 2024-10-17 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_remove_about_updated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='profile_image',
            new_name='about_image',
        ),
    ]
