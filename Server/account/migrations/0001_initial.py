# Generated by Django 4.0 on 2024-03-21 14:59

import account.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('sub', models.CharField(default=None, max_length=50, null=True, unique=True)),
                ('username', models.CharField(blank=True, default='', max_length=255, unique=True)),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('account_type', models.CharField(blank=True, default='', max_length=25)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PointDeVente',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.customuser')),
                ('lieu', models.CharField(blank=True, max_length=50)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pointdevente_related', to='account.customuser')),
            ],
            options={
                'abstract': False,
            },
            bases=('account.customuser',),
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
    ]
