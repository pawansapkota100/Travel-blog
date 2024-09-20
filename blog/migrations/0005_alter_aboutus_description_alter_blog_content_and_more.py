# Generated by Django 5.1.1 on 2024-09-20 04:28

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='whosme',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
