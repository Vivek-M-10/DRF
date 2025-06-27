from rest_framework import serializers
from watchlist.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    hit = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__' # or ['id', 'title', 'description', 'year', 'rating']
        read_only_fields = ['id']  # Make 'id' read-only if you don't want it to be editable

    def get_hit(self, obj):
        # Custom logic to determine if the movie is a hit
        if obj.rating >= 8 and obj.rating <= 9:
            return "hit"
        elif obj.rating >= 5 and obj.rating < 8:
            return "average"
        elif obj.rating > 9:
            return "blockbuster"
        else:
            return "flop"
    

    def validate_rating(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("Rating must be between 0 and 10.")
        return value
    
    def validate_year(self, value):
        if value.year < 1888:  # The first movie was made in 1888
            raise serializers.ValidationError("Year must be 1888 or later.")
        return value