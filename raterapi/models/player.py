""""Player model module"""
from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    """Player database model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)