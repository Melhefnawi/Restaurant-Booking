# Generated by Django 3.2.21 on 2023-10-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0005_auto_20231015_1146'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='booking_details',
            name='bookingsyst_Last_Na_e2af10_idx',
        ),
        migrations.RemoveIndex(
            model_name='booking_details',
            name='first_name_idx',
        ),
        migrations.AddField(
            model_name='booking_details',
            name='Booking_Id',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
