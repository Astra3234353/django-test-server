from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path('i/', views.hello_world),
  path('hello/<str:username>', views.hello_world)
]