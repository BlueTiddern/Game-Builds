"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

# login imports
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")




class StylePreferenceForm(forms.Form):
    BODY_SHAPE_CHOICES = (
        ('hourglass', 'Hourglass'),
        ('apple', 'Apple'),
        ('pear', 'Pear'),
        ('rectangle', 'Rectangle')
    )

    SKIN_TONE_CHOICES = (
        ('fair', 'Fair'),
        ('medium', 'Medium'),
        ('dark', 'Dark')
    )

    COLOR_CHOICES = (
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow')
    )

    bodyShape = forms.ChoiceField(choices=BODY_SHAPE_CHOICES, label="Select your body shape")
    skinTone = forms.ChoiceField(choices=SKIN_TONE_CHOICES, label="Select your skin tone")
    colorPreference = forms.ChoiceField(choices=COLOR_CHOICES, label="Select your color preference")


from .models import CustomerReview

class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ['name', 'rating', 'review']




