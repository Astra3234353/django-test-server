from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks

def hello_world(response, username):
  print(username)
  return render(response, 'myapp.html')

def index(response):
  title = 'django course'
  return render(response, 'index.html', {
    'title': title
  })

def project(response, id):
  projects = list(Project.objects.values())
  return JsonResponse(projects, safe=False)

def tasks(response, id):
  task = get_object_or_404(Tasks, id=id)
  return HttpResponse('tasks: %s' % task.title)