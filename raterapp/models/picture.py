"""Picture model module"""
from django.db import models


class Picture(models.Model):
    """Picture database model"""
    picture_url = models.models.URLField(max_length=200)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    