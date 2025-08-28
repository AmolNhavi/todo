from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')

def markasdone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
   # Task.objects.update(is_completed = True).filter(pk =pk) 
    return redirect('home')

def markasundone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
   # Task.objects.update(is_completed = True).filter(pk =pk) 
    return redirect('home')

def edit_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('home')
    else:
        context = {"task":task}
        return render(request,'edit_task.html',context)

def delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
    

