# Generated by Django 5.0.3 on 2024-04-05 00:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_homepage_body_remove_homepage_image_and_more'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='first_image_desc',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='second_image_desc',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='third_image_desc',
        ),
        migrations.AddField(
            model_name='homepage',
            name='first_image_description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_image_description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_image_description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='first_image',
            field=models.ForeignKey(blank=True, help_text='First photo in Carousel', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='second_image',
            field=models.ForeignKey(blank=True, help_text='Second photo in Carousel', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='third_image',
            field=models.ForeignKey(blank=True, help_text='Third photo in Carousel', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
