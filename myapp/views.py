from django.shortcuts import render, redirect
from .models import Project, Tasks
from .forms import CreateNewTask, CreateNewProject


def project(request):
  projects = Project.objects.all()
  return render(request, 'projects.html', {
    'projects': projects
  })

def tasks(request):
  tasks = Tasks.objects.all()
  return render(request, 'tasks.html', {
    'tasks': tasks
  })

def create_task(request):
  if request.method == 'GET':
    return render(request, 'create_task.html', {'form': CreateNewTask})
  else:
    Tasks.objects.create(title=request.POST['title'],
    description=request.POST['description'], project_id=2)
    return redirect('tasks')
  
def create_project(request):
  if request.method == "GET":
    return render(request, 'create_project.html', {
      'form': CreateNewProject
    })
  else:
    Project.objects.create(name=request.POST['name'])
    return redirect('project')