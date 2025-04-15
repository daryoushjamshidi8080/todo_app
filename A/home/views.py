from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm


def say_hello(request):
    return render(request, 'home/hello.html')


def home(request):
    data = Todo.objects.all()
    return render(request, 'home/home.html', context={'data': data})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'home/detail.html', context={'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo deleted successfully',
                     extra_tags='success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'],
                                body=cd['body'], created=cd['created'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()

    return render(request, 'home/create.html', {'form': form})


def update(request, todo_id):
    print(todo_id)
