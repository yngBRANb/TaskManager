from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def index(request):
    tasks = Task.objects.filter(status='active')
    return render(request, 'index.html', {'tasks': tasks})

def links(request):
    return render(request, 'link.html')

def task(request, id):
    tasks = Task.objects.get(id=id)
    return render(request, 'task.html', {'task': tasks})

def archive(request):
    tasks = Task.objects.filter(status='inactive')
    return render(request, 'archive.html', {'tasks': tasks})

@require_POST
def change_task_status(request, id):
    try:
        task = Task.objects.get(id=id)
        task.status = 'inactive'
        task.save()
        return JsonResponse({'status': 'success', 'message': 'Статус задачи изменен на неактивный.'})
    except Task.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Задача не найдена.'})
