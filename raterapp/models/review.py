"""Review model module"""
from typing import Match
from django.db import models


class Review(models.Model):
    """Review database model"""
    review_text = models.CharField(max_length=350)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    #user needs to go here
    