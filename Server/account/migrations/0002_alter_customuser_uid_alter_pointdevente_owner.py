# Generated by Django 4.0 on 2024-03-15 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='UID',
            field=models.CharField(blank=True, default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='pointdevente',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='pointdevente_related', to='account.customuser'),
        ),
    ]
