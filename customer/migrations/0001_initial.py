# Generated by Django 3.1.4 on 2020-12-17 13:25

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('access_token', models.TextField(blank=True, null=True, verbose_name='access_token')),
                ('fb_id', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='fb_id')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='phone')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='avatar')),
                ('expires_in', models.IntegerField(blank=True, null=True, verbose_name='expires_in')),
                ('is_valid_access_token', models.BooleanField(default=False, verbose_name='is_valid_access_token')),
                ('shorted_access_token', models.TextField(blank=True, null=True, verbose_name='shorted_access_token')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
