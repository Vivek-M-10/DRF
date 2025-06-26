from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.DateField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.title} ({self.year.year}) - {self.genre} by {self.director} - Rating: ({self.rating}/10)"

