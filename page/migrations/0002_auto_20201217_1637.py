# Generated by Django 3.1.4 on 2020-12-17 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={},
        ),
        migrations.AlterField(
            model_name='feed',
            name='fb_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='fb_id'),
        ),
        migrations.AlterField(
            model_name='page',
            name='access_token',
            field=models.TextField(blank=True, null=True, verbose_name='access_token'),
        ),
        migrations.AlterField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='page',
            name='fb_id',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='fb_id'),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
