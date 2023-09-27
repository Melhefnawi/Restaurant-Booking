from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Booking_details(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    People = models.IntegerField()
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Comment = models.TextField()

