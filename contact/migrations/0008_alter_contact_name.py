# Generated by Django 5.1.1 on 2024-10-19 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.TextField(max_length=20, null=True),
        ),
    ]