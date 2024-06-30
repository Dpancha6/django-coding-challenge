from rest_framework import generics # type: ignore
from movies.models import Movie, Review
from movies.serializers import MovieSerializer, ReviewSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        runtime = self.request.query_params.get('runtime', None)
        if runtime:
            operator, value = runtime[0], int(runtime[1:])
            if operator == '>':
                queryset = queryset.filter(runtime__gt=value)
            elif operator == '<':
                queryset = queryset.filter(runtime__lt=value)
        return queryset


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer