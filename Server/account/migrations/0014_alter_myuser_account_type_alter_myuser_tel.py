# Generated by Django 4.0 on 2024-03-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_myuser_account_type_alter_myuser_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='account_type',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='tel',
            field=models.TextField(blank=True, default=None),
        ),
    ]
