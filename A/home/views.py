from django.shortcuts import render
# Create your views here.
from .models import Todo


def say_hello(request):
    return render(request, 'home/hello.html')


def home(request):
    data = Todo.objects.all()
    return render(request, 'home/home.html', context={'data': data})
