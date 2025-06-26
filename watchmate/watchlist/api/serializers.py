from rest_framework import serializers
from watchlist.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'genre', 'director', 'rating']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.director = validated_data.get('director', instance.director)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
    

    