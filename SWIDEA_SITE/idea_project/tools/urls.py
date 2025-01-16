from django.urls import path
from . import views

urlpatterns = [
    path('', views.tool_list, name='tool_list'),
    
    path('<int:tool_id>/', views.tool_detail, name='tool_detail'),
    path('tool/add/', views.add_tool, name='add_tool'),
    path('tool/<int:tool_id>/edit/', views.edit_tool, name='edit_tool'),
    path('tool/<int:tool_id>/delete/', views.delete_tool, name='delete_tool'),
]