# Generated by Django 3.2.23 on 2023-12-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0020_auto_20231209_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='Phone_Number',
            field=models.TextField(null=True),
        ),
    ]