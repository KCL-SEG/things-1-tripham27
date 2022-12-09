from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(AbstractUser):
    name = models.TextField(max_length=30,unique=True,blank=False)
    description = models.TextField(max_length=120,unique=True,blank=False)
    quantity = models.IntegerField(unique=False,validators=[MinValueValidator(0),MaxValueValidator(100)])