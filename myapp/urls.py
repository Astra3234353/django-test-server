from django.urls import path
from . import views

urlpatterns = [
  path("project/", views.project, name='project'),
  path("tasks/", views.tasks, name='tasks'),
  path("create_task", views.create_task, name='create_task'),
  path("create_project", views.create_project, name='create_project')
]