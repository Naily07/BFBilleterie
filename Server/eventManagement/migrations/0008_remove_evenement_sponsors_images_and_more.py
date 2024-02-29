# Generated by Django 4.0 on 2024-02-29 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManagement', '0007_remove_sponsor_image_evenement_sponsors_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evenement',
            name='sponsors_images',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='image_url',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
