# Generated by Django 3.2.21 on 2023-10-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0006_auto_20231015_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='Booking_Id',
            field=models.IntegerField(max_length=200, null=True, unique=True),
        ),
    ]
