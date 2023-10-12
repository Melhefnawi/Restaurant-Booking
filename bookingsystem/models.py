from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Booking_details(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email = models.EmailField(null=True)
    Phone_Number = models.IntegerField(null=True)
    Date = models.DateField()
    Time = models.TimeField()
    People_No = models.IntegerField()
    body = models.TextField(null=True)
    Featured_image = CloudinaryField('image', default="placeholder")
    approved = models.BooleanField(default=False)

    class Meta:

        ordering = ['-Date']

    def __str__(self):
        return f"Booking Name: {self.First_Name} {self.Last_Name}"


class Client (models.Model):
    Booking = models.ForeignKey(Booking_details, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.IntegerField()

    def __str__(self):
        return f"Booking Name: {self.First_Name} + {self.Last_Name}"

    class Meta:

        ordering = ['-First_Name']


class Menu(models.Model):

    Featured_image = CloudinaryField('image', default="placeholder")

    def __str__(self):
        return self.Featured_image
