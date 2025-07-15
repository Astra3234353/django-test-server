from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tasks
from .forms import CreateNewTask

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

def create_task(request):
  if request.method == 'GET':
    return render(request, 'create_task.html', {'form': CreateNewTask})
  else:
    Tasks.objects.create(title=request.POST['title'],
    description=request.POST['description'], project_id=2)
    return redirect('tasks/')