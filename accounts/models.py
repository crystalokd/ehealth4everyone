from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.IntegerField()

    class Meta:
        unique_together = ('email','phone_number')


    def __str__(self):
        return self.email