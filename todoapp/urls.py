from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit-task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete-task'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle-complete'),
]