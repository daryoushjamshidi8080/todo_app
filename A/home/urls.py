from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.home, name='home'),
    path('detail/<int:todo_id>', views.detail, name='details'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('update/<int:todo_id>', views.update, name='update')
]
