# Generated by Django 3.1.4 on 2020-12-04 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='customer',
            new_name='customers',
        ),
    ]
