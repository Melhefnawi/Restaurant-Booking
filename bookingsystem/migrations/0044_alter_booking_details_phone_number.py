# Generated by Django 3.2.23 on 2024-04-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0043_alter_booking_details_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='Phone_Number',
            field=models.IntegerField(null=True),
        ),
    ]
