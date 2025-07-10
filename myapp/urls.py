from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path('hello/<str:username>', views.hello_world),
  path("project", views.project),
  path("tasks/<str:id>", views.tasks)
]