# Generated by Django 5.1.1 on 2024-09-24 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_carousel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='full_name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
        ),
    ]
