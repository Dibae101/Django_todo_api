from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Todo, name="Todo"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail")
]
