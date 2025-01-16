from django.shortcuts import render, get_object_or_404, redirect
from .models import Tool
from ideas.models import Idea  #

# 개발툴 목록
def tool_list(request):
    tools = Tool.objects.all()
    return render(request, 'tools/tool_list.html', {'tools': tools})

# 개발툴 등록
def add_tool(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        kind = request.POST.get('kind')
        content = request.POST.get('content')

        if not (name and kind and content):
            return render(request, 'tools/add_tool.html', {'error': '모든 필드를 입력하세요.'})

        tool = Tool(name=name, kind=kind, content=content)
        tool.save()
        return redirect('tool_detail', tool_id=tool.id)

    return render(request, 'tools/add_tool.html')

# 개발툴 디테일
def tool_detail(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    ideas = Idea.objects.filter(devtool=tool)  # 해당 개발툴을 참조하는 아이디어 목록
    print(f"Tool: {tool.name}")  # 개발툴 이름 출력
    print(f"Ideas: {ideas}")    # 관련된 아이디어 출력
    return render(request, 'tools/tool_detail.html', {'tool': tool, 'ideas': ideas})

# 개발툴 수정
def edit_tool(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)

    if request.method == 'POST':
        tool.name = request.POST.get('name')
        tool.kind = request.POST.get('kind')
        tool.content = request.POST.get('content')
        tool.save()
        return redirect('tool_detail', tool_id=tool.id)

    return render(request, 'tools/edit_tool.html', {'tool': tool})

# 개발툴 삭제
def delete_tool(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    if request.method == 'POST':
        tool.delete()
        return redirect('tool_list')

    return render(request, 'tools/delete_tool.html', {'tool': tool})