# Generated by Django 3.2.21 on 2023-10-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0007_alter_booking_details_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='Booking_Id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
