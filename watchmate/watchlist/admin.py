from django.contrib import admin
from .models import Movie
   

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'director', 'rating_out_of_ten')
    search_fields = ('title', 'director')
    list_filter = ('year', 'genre')
    ordering = ('-year', 'title')

    def rating_out_of_ten(self, obj):
        return f"{obj.rating}/10"

    rating_out_of_ten.short_description = 'Rating'

admin.site.register(Movie, MovieAdmin)
