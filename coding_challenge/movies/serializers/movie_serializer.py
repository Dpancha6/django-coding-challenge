from rest_framework import serializers # type: ignore

from movies.models import Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    class Meta:
        model = Review
        fields = ['movie', 'name', 'rating']

class NestedReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'rating']
   
class MovieSerializer(serializers.ModelSerializer):
    reviewers = NestedReviewSerializer(many=True, read_only=True)
    runtime_formatted = serializers.ReadOnlyField()
    avg_rating = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            "avg_rating",
            "reviewers",
        )
