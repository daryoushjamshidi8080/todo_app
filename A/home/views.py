from django.shortcuts import render
# Create your views here.


def say_hello(request):
    return render(request, 'home/hello.html')


def home(request):
    person = {
        'name': 'amir',
        'age': 25
    }
    return render(request, 'home/home.html', context={'person': person, 'h1': 'ali'})
