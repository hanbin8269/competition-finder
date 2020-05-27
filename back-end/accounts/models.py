from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
)
# Create your models here.
class User(AbstractBaseUser):

    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True,
    )
    
    is_superuser = False

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']