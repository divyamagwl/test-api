from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    User model with extra information while Django still handles the authentication process
    """
    email = models.EmailField(blank=False, max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=10, verbose_name="Phone number")