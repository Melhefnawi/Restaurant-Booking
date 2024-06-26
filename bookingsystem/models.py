from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator



# Create your models here.

# Booking details model to obtain the Booking details from 
# User and store it in the Data base 



class Booking_details(models.Model):
    
    Phone_Number = models.IntegerField(null=True)
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking", null=True
    )                                          
    Date = models.DateField()
    Time = models.TimeField()
    People_No = models.IntegerField()
    approved = models.BooleanField(default=False)

    class Meta:

        ordering = ['-Date']
       
    def __str__(self):
        return f"Booking Name: {self.User} "

# Menu Model to store the data related to Menu


class Menu(models.Model):

    Featured_image = CloudinaryField('image', default="placeholder")
    Meal_Name = models.CharField(max_length=200, null=True)
    Meal_des = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"Image Name: {self.Meal_Name}"
