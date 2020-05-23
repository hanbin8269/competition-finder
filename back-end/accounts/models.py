from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)
# Create your models here.
class User(AbstractUser):

    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True,
    )
    

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']