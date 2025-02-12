from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def list_task(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/todo_list.html', context)

def create_todo(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('todo:todo_list')
    context = {
        'form': form
    }
    return render(request, 'todo/create_todo.html', context)

def todo_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/todo_detail.html', {'form': form, 'task': task})

def delete_todo(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo:todo_list')

# Create your views here.
