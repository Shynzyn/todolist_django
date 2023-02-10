from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    task = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

