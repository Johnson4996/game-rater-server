"""Rating model module"""
from django.db import models


class Rating(models.Model):
    """Rating database model"""
    rate = models.IntegerField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    #user needs to go here
    