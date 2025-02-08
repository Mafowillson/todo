from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.list_task, name='todo_list'),
    path('todo/create/', views.create_todo, name = 'create_todo'),
    path('todo/<int:task_id>/', views.todo_detail, name='todo_detail'),
    path('todo/<int:task_id>/delete/', views.delete_todo, name='delete_todo'),
]