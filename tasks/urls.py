from django.urls import path
from . import views

urlpatterns = [
    path('list_create/', views.ListCreateTasks.as_view()),
    path('task_detail/<int:pk>/', views.TaskDetail.as_view()),
]
