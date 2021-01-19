from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import viewsets
from django.views.generic import ListView, TemplateView
from django.contrib.auth.models import User


# APIs
class ProjectView(viewsets.ModelViewSet):
    '''
    Crud APIs for project
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskView(viewsets.ModelViewSet):
    '''
    Crud APIs for task
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Views for pages
class ProjectList(ListView):
    '''
    for listing all the projects
    '''
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/projects.html'


class ProjectNewView(TemplateView):
    '''
    render template for new/edit project
    '''
    template_name = 'projects/project_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectNewView, self).get_context_data(*args, **kwargs)
        context["tasks"] = Task.objects.filter(
                                            project=kwargs.get('id'),
                                            parent__isnull=True)
        context["project"] = Project.objects.filter(
                                                id=kwargs.get('id')).first()
        return context


class TaskNewView(TemplateView):
    '''
    render template for new/edit task
    '''
    template_name = 'projects/task_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaskNewView, self).get_context_data(*args, **kwargs)
        context["projects"] = Project.objects.all()
        context["task"] = Task.objects.filter(id=kwargs.get('task_id')).first()
        context["users"] = User.objects.all()
        return context
