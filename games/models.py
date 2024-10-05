from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Game(models.Model):
    """
    Game model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    genre_filter_choices = [
    ('none', 'none'),
    ('family', 'Family Game'),
    ('dexterity', 'Dexterity Game'),
    ('party', 'Party Game'),
    ('abstract', 'Abstract Game'),
    ('thematic', 'Thematic Game'),
    ('eurogame', 'Eurogame'),
    ('wargame', 'Wargame'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    designer = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    min_players = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    max_players = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    solo_play = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ynmksg', blank=True
    )
    genre_filter = models.CharField(
        max_length=32, choices=genre_filter_choices, default='none'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    def clean(self):
        if self.min_players > self.max_players:
            raise ValidationError('Minimum players cannot be greater than maximum players.')

    def __str__(self):
        return f'{self.min_players}-{self.max_players} players'
