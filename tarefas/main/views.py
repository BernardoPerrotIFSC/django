from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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


@login_required
def index(request, id):
    lista = ToDoList.objects.get(id=id)

    if request.method == 'POST':
        if request.POST.get("save"):
            for item in lista.item_set.all():
                if request.POST.get("c"+ str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()
        elif request.POST.get("newItem"):
            text = request.POST.get("new")

            if len(text)>2:
                lista.item_set.create(text = text, complete= False)
            else:
                print("invalid")
            
        return redirect("/%i" % lista.id)

    return render(request, 'main/list.html', {'lista':lista})

@login_required
def home(response):
    return render(response, 'main/home.html')

@login_required
def view(request):
    return render(request, "main/view.html")



