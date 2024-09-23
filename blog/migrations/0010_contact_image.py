# Generated by Django 5.1.1 on 2024-09-23 13:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_contact_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Contact'),
        ),
    ]