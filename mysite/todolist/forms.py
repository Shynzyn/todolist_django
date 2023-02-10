from .models import Task
from django import forms
from django.contrib.auth.models import User


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task']