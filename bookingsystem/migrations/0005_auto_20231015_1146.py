# Generated by Django 3.2.21 on 2023-10-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0004_menu_meal_name'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='booking_details',
            index=models.Index(fields=['Last_Name', 'First_Name'], name='bookingsyst_Last_Na_e2af10_idx'),
        ),
        migrations.AddIndex(
            model_name='booking_details',
            index=models.Index(fields=['First_Name'], name='first_name_idx'),
        ),
    ]