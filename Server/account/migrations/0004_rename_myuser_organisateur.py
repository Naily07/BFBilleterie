# Generated by Django 4.0 on 2024-03-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0003_remove_myuser_account_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='Organisateur',
        ),
    ]
