from django.db import models

# Create your models here.

class Player(models.Model):
    gamertag = models.CharField(max_length = 50 , unique = True)
    age = models.PositiveBigIntegerField()
    discord = models.CharField(max_length = 50 , unique = True)

    def __str__(self):
     return self.gamertag


