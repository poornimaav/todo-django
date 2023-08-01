from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q
# Create your views here.

def index(request):

    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'todo/list.html', context)


def create(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'todo/create.html', context)

def view(request,pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    context = {'form': form, 'tasks':tasks}
    return render(request, 'todo/view.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    context = {'form': form}
    return render(request, 'todo/update.html', context)


def delete(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('list')
