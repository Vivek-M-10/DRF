from calendar import c
from django.contrib import admin
from .models import Watchlist, StreamPlatform, Review
   

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'director', 'rating', 'created_at')
    search_fields = ('title', 'director')
    list_filter = ('year', 'genre')
    ordering = ('-created_at',)

class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'website')
    search_fields = ('name',)
    ordering = ('name',) 
    list_filter = ('name',)  

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('watchlist', 'rating', 'created_at')
    search_fields = ('watchlist__title',)
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',) 

admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(StreamPlatform, StreamPlatformAdmin)
admin.site.register(Review, ReviewAdmin)
