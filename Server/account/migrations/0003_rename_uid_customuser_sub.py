# Generated by Django 4.0 on 2024-03-15 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_uid_alter_pointdevente_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='UID',
            new_name='sub',
        ),
    ]
