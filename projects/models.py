from django.db import models
from django.contrib.auth.models import User
import os


def get_avatar_url(instance, filename):
    return os.path.join('project', instance.name)


class Project(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    duration = models.IntegerField()
    avatar = models.ImageField(upload_to=get_avatar_url)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True)
    name = models.CharField(max_length=512)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True)

    def __str__(self):
        return self.name
