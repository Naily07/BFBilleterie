# Generated by Django 5.0.3 on 2024-03-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManagement', '0004_ticketqrcode_type_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='type_event',
            field=models.TextField(blank=True, default='', max_length=50),
        ),
    ]
