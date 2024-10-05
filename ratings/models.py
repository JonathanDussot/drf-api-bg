from django.db import models
from django.contrib.auth.models import User
from games.models import Game

class Rating(models.Model):
    """ 
    Rating model with related name ratings
    """
    rating = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.game}'