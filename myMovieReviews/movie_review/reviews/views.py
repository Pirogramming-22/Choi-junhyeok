from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from django.http import HttpResponse
from django.db.models import Avg


def index(request):
    movies = Movie.objects.all()
    movie_data = []

    for movie in movies:
        average_rating = movie.review_set.aggregate(Avg('rating'))['rating__avg'] or 0
        movie_data.append({
            'movie': movie,
            'average_rating': round(average_rating, 1),
            'release_date': movie.release_date  # 개봉년도 추가
        })

    return render(request, 'reviews/index.html', {'movie_data': movie_data})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    return render(request, 'reviews/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'average_rating': round(average_rating, 1),  # 평균 별점 전달
    })

def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')

        if not title or not release_date or not genre:
            return HttpResponse("모든 필드를 입력해야 합니다.", status=400)

        # 영화 저장
        movie = Movie(title=title, release_date=release_date, genre=genre)
        movie.save()

        return redirect('index')  # 영화 목록으로 리디렉션

    return render(request, 'reviews/add_movie.html')

def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        reviewer = request.POST.get('reviewer')
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        if not reviewer or not content or not rating:
            return HttpResponse("모든 필드를 입력해야 합니다.", status=400)

        # 리뷰 저장
        review = Review(movie=movie, reviewer=reviewer, content=content, rating=rating)
        review.save()

        return redirect('movie_detail', movie_id=movie.id)

    return render(request, 'reviews/add_review.html', {'movie': movie})

def add_movie_with_review(request):
    if request.method == 'POST':
        # 영화 정보 가져오기
        title = request.POST.get('title')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        director = request.POST.get('director')
        actors = request.POST.get('actors')
        runtime = request.POST.get('runtime')  # 러닝타임 가져오기

        # 리뷰 정보 가져오기
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        # 입력 값 검증
        if not (title and release_date and genre and director and actors and runtime and content and rating):
            return render(request, 'reviews/add_movie_with_review.html', {
                'error': "모든 필드를 입력해야 합니다."
            })

        try:
            # 영화 저장
            movie = Movie(
                title=title,
                release_date=release_date,
                genre=genre,
                director=director,
                actors=actors,
                runtime=runtime  # 러닝타임 저장
            )
            movie.save()

            # 리뷰 저장
            review = Review(movie=movie, content=content, rating=int(rating))
            review.save()
        except Exception as e:
            return render(request, 'reviews/add_movie_with_review.html', {
                'error': f"저장 중 오류가 발생했습니다: {e}"
            })

        return redirect('index')

    return render(request, 'reviews/add_movie_with_review.html')
# 영화 수정
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = movie.review_set.first()  # 첫 번째 리뷰만 가져옴

    if request.method == 'POST':
        # 영화 정보 업데이트
        movie.title = request.POST.get('title')
        movie.release_date = request.POST.get('release_date')
        movie.genre = request.POST.get('genre')
        movie.director = request.POST.get('director')  # 감독 업데이트
        movie.actors = request.POST.get('actors')  # 배우 업데이트
        movie.runtime = request.POST.get('runtime')  # 러닝타임 업데이트
        movie.save()

        # 리뷰 정보 업데이트 (있는 경우)
        if review:
            review.content = request.POST.get('review')  # 리뷰 내용 업데이트
            review.rating = request.POST.get('rating')  # 평점 업데이트
            review.save()

        return redirect('movie_detail', movie_id=movie.id)

    return render(request, 'reviews/edit_movie.html', {
        'movie': movie,
        'review': review,
        'average_rating': review.rating if review else 0
    })
# 영화 삭제
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index')

    return render(request, 'reviews/delete_movie.html', {'movie': movie})

