from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    genre_filter_choices = [
    ('family', 'Family Game'),
    ('dexterity', 'Dexterity Game'),
    ('party', 'Party Game'),
    ('abstract', 'Abstract Game'),
    ('thematic', 'Thematic Game'),
    ('eurogame', 'Eurogame'),
    ('wargame', 'Wargame'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    designer = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ynmksg', blank=True
    )
    genre_filter = models.CharField(
        max_length=32, choices=genre_filter_choices, default='normal'
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'