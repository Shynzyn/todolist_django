from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import TaskCreateForm
from .models import Task


def index(request):
    return render(request, 'index.html')


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    success_url = '/tasks/'
    template_name = 'add_task.html'
    form_class = TaskCreateForm
    # fields = ['task']

    def form_valid(self, form):
        print("AAAAA")
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    success_url = '/tasks/'
    template_name = 'add_task.html'
    form_class = TaskCreateForm

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user

    def form_valid(self, form):
        form.instance.reader = self.request.user
        form.save()
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    success_url = '/tasks/'
    template_name = 'delete_task.html'
    context_object_name = 'task'

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user
#
