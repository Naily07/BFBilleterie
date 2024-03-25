# Generated by Django 5.0.3 on 2024-03-25 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketQrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_image', models.ImageField(upload_to='qr_code_img/')),
                ('num', models.DecimalField(decimal_places=0, max_digits=6)),
                ('ID_ticket', models.DecimalField(decimal_places=0, max_digits=5)),
                ('is_disabled', models.BooleanField(default=False)),
                ('addOwner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_related', to='eventManagement.evenement')),
            ],
        ),
    ]