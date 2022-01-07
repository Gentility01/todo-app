from django.shortcuts import redirect, render

import todo
from .models import TodoListItem
from django.views.decorators.http import require_POST
from .forms import TodoForm

# Create your views here.
def homeview(request):
    listform = TodoForm()
    todolist = TodoListItem.objects.order_by('id')
    context = {
        'todo' : todolist,
        'todo_form': listform
    }
    return render(request, 'todo/index.html', context)

 
@require_POST
def addTodoView(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = TodoListItem(content=request.POST['content'])
        new_todo.save()
        
    return redirect('home')


def complete_todo(request, todo_id):
    todo = TodoListItem.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('home')

def deleteCompleted(request):
    TodoListItem.objects.filter(complete__exact=True).delete()
    

    return redirect('home')

def deleteAll(request):
    TodoListItem.objects.all().delete()
    return redirect('home')
  
