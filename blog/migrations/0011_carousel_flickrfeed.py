# Generated by Django 5.1.1 on 2024-09-24 03:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_contact_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Carousel')),
            ],
        ),
        migrations.CreateModel(
            name='FlickrFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='FlickrFeed')),
            ],
        ),
    ]