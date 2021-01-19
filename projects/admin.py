from django.contrib import admin
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    list_filter = ('assignee', 'parent')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
