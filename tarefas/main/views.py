from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def create(request):
    form = CreateNewList()
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            todo = ToDoList(name=name)
            todo.save()
            request.user.todolist.add(todo)
            return redirect("/%i" % todo.id)
        else:
            form = CreateNewList()

    return render(request, 'main/create.html', {"form":form})
    # form = CreateNewList()
    # return render(request, "main/create.html",{"form":form})



def index(request, id):
    lista = ToDoList.objects.get(id=id)
    return render(request, 'main/list.html', {'lista':lista})

def home(reponse):
    return render(reponse, 'main/home.html')


