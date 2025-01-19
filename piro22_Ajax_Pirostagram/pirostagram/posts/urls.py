from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 게시글 목록
    path('post/<int:post_id>/', views.detail, name='detail'),  # 게시글 상세
    path('post/create/', views.create, name='create'),  # 게시글 생성
    path('post/<int:post_id>/edit/', views.edit, name='edit'),  # 게시글 수정
    path('post/<int:post_id>/delete/', views.delete, name='delete'),  # 게시글 삭제
    path('post/<int:post_id>/like_ajax/', views.like_post_ajax, name='like_post_ajax'),
    path('post/<int:post_id>/comment/add/', views.add_comment, name='add_comment'),  # 댓글 작성
    path('post/<int:post_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),  # 댓글 삭제
]