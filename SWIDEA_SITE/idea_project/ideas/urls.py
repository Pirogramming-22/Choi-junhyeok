from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('add/', views.add_idea, name='add_idea'),
    path('<int:idea_id>/', views.idea_detail, name='idea_detail'),
    path('<int:idea_id>/edit/', views.edit_idea, name='edit_idea'),
    path('<int:idea_id>/delete/', views.delete_idea, name='delete_idea'),
    path('<int:idea_id>/star/', views.toggle_star, name='toggle_star'),
    path('<int:idea_id>/interest/', views.update_interest, name='update_interest'),
]

