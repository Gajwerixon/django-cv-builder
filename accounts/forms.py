from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """User Register Form"""

    # Basic form don't have email field
    email = forms.EmailField()
    
    class Meta:
        """
        Internal configuration class (metadata).
        It tells django, how to link database with form.
        """

        # If everything goes fine, the data should be save in database
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)