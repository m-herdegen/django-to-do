from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('todos/new', views.new_todo),
    path('todos', views.create_todo)
]