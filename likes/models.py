from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class Like(models.Model):
    """
    Like model, related to 'owner' and 'game'.
    'owner' is a User instance and 'game' is a Game instance.
    'unique_together' makes sure a user can't like the same game twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'game']

    def __str__(self):
        return f'{self.owner} {self.game}'