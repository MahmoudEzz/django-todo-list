from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Retrive all tasks and display it in home page
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = { 
        'tasks': tasks,
        'form': form
        }
    return render(request, 'tasks/index.html', context)

# Add a task then redirect to index to display all tasks
def addTask(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = Task(text = request.POST['text'])
        new_task.save()
    return redirect('index')

# Make a task done 
def checked(request, id):
    task = Task.objects.filter(id=id)
    if not task:
        return redirect('index')
    task.done = True
    task.save()    
    return redirect('index')
    
# Display all done tasks
def done(request):
    doneTasks = Task.objects.filter(done__exact = True)
    form = TaskForm()
    context = { 
        'tasks': doneTasks,
        'form': form
        }
    return render(request, 'tasks/index.html', context)

# Display all active tasks
def active(request):
    doneTasks = Task.objects.filter(done__exact = False)
    form = TaskForm()
    context = { 
        'tasks': doneTasks,
        'form': form
        }
    return render(request, 'tasks/index.html', context)

# Delete all the tasks 
def deleteAll(request):
    tasks = Task.objects.all()
    tasks.delete()
    return redirect('index')

# Delete a task with a specific id 
def deleteOne(request, id):
    task = Task.objects.filter(id=id)
    if not task:
        return redirect('index')
    task.delete()
    return redirect('index')