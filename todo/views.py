from venv import create
from django.shortcuts import render, redirect

from todo.models import Todo
# import datetime
from django.utils import timezone
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title'],
            created_at = timezone.now(),
        )
        new_todo.save()
        return redirect('/')
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)


def delete( request, pk):
    delete_todo = Todo.objects.get(id=pk)
    delete_todo.delete()
    return redirect('/')

