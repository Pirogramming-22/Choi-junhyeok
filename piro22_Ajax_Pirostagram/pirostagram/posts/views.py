from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

# 게시글 목록
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

# 게시글 상세
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

# 게시글 생성
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('index')
    return render(request, 'posts/create.html')

# 게시글 수정
def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('detail', post_id=post.id)
    return render(request, 'posts/edit.html', {'post': post})

# 게시글 삭제
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'posts/delete.html', {'post': post})

# 게시글 좋아요
from django.http import JsonResponse

def like_post_ajax(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, content=content)
    return redirect('detail', post_id=post.id)

# 댓글 삭제
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    if request.method == 'POST':
        comment.delete()
    return redirect('detail', post_id=post_id)