from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)  # 게시글 제목
    content = models.TextField()  # 게시글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간
    likes = models.PositiveIntegerField(default=0)  # 좋아요 수 (기본값 0)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # 게시글과 연결
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 댓글 작성 시간

    def __str__(self):
        return f'Comment on {self.post.title}'