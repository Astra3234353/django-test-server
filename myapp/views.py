from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Tasks

def hello_world(response, username):
  print(username)
  return render(response, 'myapp.html')

def index(response):
  title = 'django course'
  return render(response, 'index.html', {
    'title': title
  })

def project(response):
  projects = Project.objects.all()
  return render(response, 'projects.html', {
    'projects': projects
  })

def tasks(response):
  tasks = Tasks.objects.all()
  return render(response, 'tasks.html', {
    'tasks': tasks
  })