from tkinter import W
from watchlist.models import Watchlist, StreamPlatform, Review
from rest_framework import serializers

# Ensure the import path is correct based on your project structure

class WatchlistSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Watchlist
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):

    # watchlist = WatchlistSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review  # Use the through model for the many-to-many relationship
        fields = '__all__'
        read_only_fields = ('watchlist',)  # Make watchlist read-only if you don't want to allow creation of reviews directly through it