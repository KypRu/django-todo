from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.

def task_list(request):
    status = request.GET.get('status')
    if status == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif status == 'active':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    return render(request, 'todoapp/task_list.html', {
        'tasks': tasks,
        'status': status,
    })

    
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'todoapp/add_task.html', {'form': form})
    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'todoapp/delete_task.html', {'task': task})
    
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')
