from django.urls import path
from rest_framework import routers
from .views import ProjectView, TaskView, ProjectList, \
    ProjectNewView, TaskNewView


router = routers.DefaultRouter()
router.register(r'api/project', ProjectView)
router.register(r'api/task', TaskView)

urlpatterns = [
    path('', ProjectList.as_view()),
    path('project/new', ProjectNewView.as_view()),
    path('project/<int:id>', ProjectNewView.as_view()),
    path('project/<int:project_id>/task/<int:task_id>', TaskNewView.as_view()),
    path('project/<int:project_id>/task/new', TaskNewView.as_view()),
]
urlpatterns += router.urls
