from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    A form for registering new users, extending Django's UserCreationForm.
    Fields:
        email (EmailField): Required email address for the user.
    Meta:
        model (User): The user model to create.
        fields (list): List of fields to include in the form: 'username', 'email', 'password1', 'password2'.
    """
    email = forms.EmailField(required=True)  # Make email required

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
