from rest_framework import serializers
from watchlist.models import Movie

def rating_validator(value):
    if value < 0 or value > 10:
        raise serializers.ValidationError("Rating must be between 0 and 10.")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    year = serializers.DateField()
    genre = serializers.CharField()
    director = serializers.CharField()
    rating = serializers.FloatField(validators=[rating_validator])

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
    
    # def validate_rating(self, value):
    #     if value < 0 or value > 10:
    #         raise serializers.ValidationError("Rating must be between 0 and 10.")
    #     return value
    
    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError("Title is required.")
        if not data.get('year'):
            raise serializers.ValidationError("Year is required.")
        if not data.get('genre'):
            raise serializers.ValidationError("Genre is required.")
        if not data.get('director'):
            raise serializers.ValidationError("Director is required.")
        return data
        


    