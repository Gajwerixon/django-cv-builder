from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Gets our email-driven CustomUser model instead of Django's default User model.
User = get_user_model()


class RegisterForm(UserCreationForm):
    """
    User registration form. It inherits from UserCreationForm,
    which guarantees automatic and secure password hashing.
    """

    # Override the email field: make it required and add a placeholder
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.EmailInput(
            attrs={"placeholder": "Email"}
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First name"}
        ),
        label=""
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last name"}
        ),
        label=""
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}
        )
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm password"}
        )
    )


    class Meta(UserCreationForm.Meta):
        """
        Configuration class (metadata). Inherits from UserCreationForm.Meta
        to preserve Django's built-in password validation mechanisms.
        """

        model = User
        # List of fields that the form will render and process.
        fields = ("email", "first_name", "last_name", "password1", "password2")