from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """Custom manager to handle user creation without a username field."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a standard User with the given email and password."""

        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        # Initialize the user instance using the CustomUser model
        user = self.model(
            email=email,
            **extra_fields
        )

        # Encrypt (hash) the password securely before saving
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a Superuser with the given email and password."""

        # Ensure administrative permissions are enabled by default
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(
            email,
            password,
            **extra_fields
        )

class CustomUser(AbstractUser):
    """Custom User model where email is the unique identifier for authentication."""
    
    username = None

    email = models.EmailField(unique=True)

    # Link the model to the custom manager defined above
    objects = CustomUserManager()

    # Set email as the primary login identifier instead of a username
    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = ["first_name", "last_name"]