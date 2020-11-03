"""Game model module"""
from django.db import models

class Game(models.Model):
    """Game database module"""
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=20)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_rec = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)