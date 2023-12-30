"""
Definition of models.
"""

from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Create your models here.

class Profile(models.Model):
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        # Add more if needed
    )

    SHAPE_CHOICES = (
        ('Ectomorph', 'Ectomorph'),
        ('Mesomorph', 'Mesomorph'),
        ('Endomorph', 'Endomorph'),
        # Add more if needed
    )

    SKIN_TYPE_CHOICES = (
        ('Fair', 'Fair'),
        ('Medium', 'Medium'),
        ('Dark', 'Dark'),
        # Add more if needed
    )

    COLOR_CHOICES = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        # Add more if needed
    )

    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    shape = models.CharField(max_length=50, choices=SHAPE_CHOICES, default='Ectomorph')
    skin_type = models.CharField(max_length=50, choices=SKIN_TYPE_CHOICES, default='Fair')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='Red')
    image = models.ImageField(upload_to='profile_images/', default='placeholder.jpg')

    def __str__(self):
        return self.gender + ' ' + self.shape + ' ' + self.skin_type + ' ' + self.color

class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()