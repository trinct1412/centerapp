# Generated by Django 3.1.4 on 2020-12-13 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20201204_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='acess_token',
            new_name='access_token',
        ),
    ]
