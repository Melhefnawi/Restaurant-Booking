# Generated by Django 3.2.23 on 2023-12-09 19:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0017_alter_booking_details_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='Phone_Number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=18, null=True, region=None),
        ),
    ]
