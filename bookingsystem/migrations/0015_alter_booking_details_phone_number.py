# Generated by Django 3.2.23 on 2023-12-09 12:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0014_alter_booking_details_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
