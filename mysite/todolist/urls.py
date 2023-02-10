from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/create', views.TaskCreateView.as_view(), name="create"),
    path('tasks/<int:pk>/update', views.TaskUpdateView.as_view(), name="update"),
    path('tasks/<int:pk>/delete', views.TaskDeleteView.as_view(), name="delete"),
]
