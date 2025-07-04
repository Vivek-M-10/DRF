
import platform
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Watchlist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    year = models.DateField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey('StreamPlatform', related_name='watchlist', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.year.year}) - {self.genre} by {self.director} - Rating: ({self.rating}/10)"
    
class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    website = models.URLField(max_length=200)
    

    def __str__(self):
        return self.name
    
class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(max_length=500)
    watchlist = models.ForeignKey(Watchlist, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.watchlist.title} - Rating: {self.rating}/5"