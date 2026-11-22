from django.db import models
from django.contrib.auth.models import AbstractUser

# CUSTOM AUTH USER MODEL
class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
