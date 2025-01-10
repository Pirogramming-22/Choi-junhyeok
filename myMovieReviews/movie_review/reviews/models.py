from django.db import models

from django.db import models



class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.IntegerField()  # 연도만 저장
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100, default="Unknown")  # 감독 필드 추가
    actors = models.TextField(default="Unknown")  # 배우 필드 추가
    runtime = models.IntegerField(default=0)  # 러닝타임 (분)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reviewer} - {self.movie.title}'