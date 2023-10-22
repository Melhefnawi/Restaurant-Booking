from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# Booking details model to obtain the Booking details from 
# User and store it in the Data base 


class Booking_details(models.Model):
    Booking_Id = models.IntegerField(unique=True, null=True)
    Slug = models.SlugField(unique=True, null=True)
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

# Menu Model to store the data related to Menu


class Menu(models.Model):

    Featured_image = CloudinaryField('image', default="placeholder")
    Meal_Name = models.CharField(max_length=200, null=True)
    Meal_des = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"Image Name: {self.Meal_Name}"
