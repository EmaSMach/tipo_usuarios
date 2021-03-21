from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('normal', 'Normal'),
        ('parcial', 'Parcial'),
    ]
    dni = models.IntegerField('Dni', primary_key=True)
    tipo = models.CharField(max_length=10, choices=USER_TYPES)


