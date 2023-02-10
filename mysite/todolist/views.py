from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Task


#
# @login_required
# def tasks(request):
#     tasks = Task.objects.filter(user=request.user)
#     return render(request, 'tasks.html', {'tasks': tasks})

def index(request):
    return render(request, 'index.html')


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = "tasks"
