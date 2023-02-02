from django.shortcuts import render, redirect

from home.models import Todo


# main page
def index(request):
    todos = Todo.objects.all()
    data = {
        'todos': todos,
    }
    return render(request, "index.html", data)


# add function


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")

        todo = Todo(name=name, desc=description, price=price)
        if len(name) != 0 and len(description) != 0 and len(price) != 0:

            todo.save()
        else:
            return redirect("index")
    return redirect("index")

# edit function


def edit(request, Id):
    data = Todo.objects.get(pk=Id)
    return render(request, "edit.html", {'data': data})


# delete function
def delete(request, Id):
    s = Todo.objects.get(pk=Id)
    s.delete()
    return redirect("index")


# for view specific data
def viewData(request, Id):
    x = Todo.objects.filter(pk=Id)
    data = {
        'x': x,
    }
    return render(request, "ViewData.html", data)


# when we click on update
def do_update_record(request, Id):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        s = Todo.objects.get(pk=Id)
        s.name = name
        s.desc = desc
        s.price = price
        if len(name) != 0 and len(desc) != 0 and len(price) != 0:
            s.save()
        else:
            return redirect("edit")
    return redirect('index')
