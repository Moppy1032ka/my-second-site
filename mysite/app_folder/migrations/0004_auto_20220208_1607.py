# Generated by Django 3.0.7 on 2022-02-08 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_folder', '0003_auto_20200625_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='upload date'),
        ),
    ]
