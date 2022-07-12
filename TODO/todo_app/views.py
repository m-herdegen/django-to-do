from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todo_app/index.html', context)

def new_todo(request):
    return render(request, 'todo_app/form.html')

def create_todo(request):
    print('create_todo')

    if request.method == 'POST':
        try: 
            body = json.loads(request.body)
            Todo.objects.create_todo()
            print('creation success')
            return JsonResponse({'success': True})
        except Exception as e:
            print('\n:(\n',str(e))
            return JsonResponse({'success': False})