from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Idea, IdeaStar
from tools.models import Tool


# 아이디어 목록
# 아이디어 목록
def idea_list(request):
    # 정렬 기준 가져오기
    sort_by = request.GET.get('sort_by', '-id')  # 기본값: 최신순
    valid_sort_fields = ['id', '-id', 'interest', '-interest', 'title', '-title', 'created_at', '-created_at']

    # 잘못된 정렬 값 방지
    if sort_by not in valid_sort_fields:
        sort_by = '-id'

    # 정렬 적용
    ideas = Idea.objects.all().order_by(sort_by)

    # 페이지네이션 설정
    paginator = Paginator(ideas, 4)  # 페이지당 4개
    page = request.GET.get('page', 1) 
    ideas = paginator.get_page(page)

    # 템플릿에 정렬 기준 및 아이디어 전달
    return render(request, 'ideas/idea_list.html', {
        'ideas': ideas,
        'sort_by': sort_by,
    })


# 아이디어 상세
def idea_detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    star = IdeaStar.objects.filter(idea=idea).first()
    return render(request, 'ideas/idea_detail.html', {'idea': idea, 'star': star})


# 아이디어 등록
def add_idea(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        interest = request.POST.get('interest', 0)
        devtool_id = request.POST.get('devtool')
        image = request.FILES.get('image')  # 이미지 파일 가져오기 (없으면 None)
        devtool = Tool.objects.get(id=devtool_id) if devtool_id else None

        idea = Idea.objects.create(
            title=title,
            content=content,
            interest=interest,
            devtool=devtool,
            image=image if image else None,)  # 이미지가 없으면 None
        IdeaStar.objects.create(idea=idea)
        return redirect('idea_detail', idea_id=idea.id)

    tools = Tool.objects.all()
    return render(request, 'ideas/add_idea.html', {'tools': tools})


# 아이디어 수정
def edit_idea(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)

    if request.method == 'POST':
        idea.title = request.POST.get('title')
        idea.content = request.POST.get('content')
        idea.interest = request.POST.get('interest', 0)
        devtool_id = request.POST.get('devtool')
        idea.devtool = Tool.objects.get(id=devtool_id) if devtool_id else None
        if 'image' in request.FILES:
            idea.image = request.FILES['image']  # 새 이미지로 업데이트
        idea.save()
        return redirect('idea_detail', idea_id=idea.id)

    tools = Tool.objects.all()
    return render(request, 'ideas/edit_idea.html', {'idea': idea, 'tools': tools})


# 아이디어 삭제
def delete_idea(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')

    return render(request, 'ideas/delete_idea.html', {'idea': idea})


# 찜하기 기능
def toggle_star(request, idea_id):
    print(f"Toggle star request received for idea ID: {idea_id}")
    idea = get_object_or_404(Idea, id=idea_id)
    star, created = IdeaStar.objects.get_or_create(idea=idea)
    star.is_starred = not star.is_starred
    star.save()
    print(f"IdeaStar state: {star.is_starred}")
    return JsonResponse({'is_starred': star.is_starred})

# 관심도 조정 기능 디버깅
def update_interest(request, idea_id):
    print(f"Update interest request received for idea ID: {idea_id}")
    idea = get_object_or_404(Idea, id=idea_id)
    change = int(request.GET.get('change', 0))
    print(f"Interest change: {change}")
    idea.interest += change
    idea.save()
    print(f"New interest value: {idea.interest}")
    return JsonResponse({'interest': idea.interest})