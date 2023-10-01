# Generated by Django 3.2.21 on 2023-09-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('People', models.IntegerField()),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('Comment', models.TextField()),
            ],
        ),
    ]