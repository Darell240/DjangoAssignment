from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST' and request.POST.get('title'):
        Task.objects.create(title=request.POST['title'].strip())
    return redirect('task_list')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('task_list')