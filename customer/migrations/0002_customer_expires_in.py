# Generated by Django 3.1.4 on 2020-12-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='expires_in',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
