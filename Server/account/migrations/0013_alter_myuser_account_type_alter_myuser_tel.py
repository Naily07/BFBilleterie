# Generated by Django 4.0 on 2024-03-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_myuser_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='account_type',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='tel',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
    ]