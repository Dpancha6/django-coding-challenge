from django.db import models # type: ignore


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    runtime = models.PositiveIntegerField()
    release_date = models.DateField()

    @property
    def runtime_formatted(self):
        hours, minutes = divmod(self.runtime, 60)
        return f"{hours}:{minutes:02}"

    @property
    def avg_rating(self):
        reviewers = self.reviewers.all()
        if reviewers:
            return sum(review.rating for review in reviewers) / reviewers.count()
        return 0


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviewers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()

