from django.urls import path # type: ignore

from movies.views import MovieListView, MovieDetailView, ReviewCreateView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path("<int:pk>/", MovieDetailView.as_view(), name="MovieDetailView"),
    path("reviews/", ReviewCreateView.as_view(), name="ReviewCreateView"),
]
