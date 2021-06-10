from django.shortcuts import render, redirect
from .models import item

# Create your views here.


def get_todo_list(request):
    items = item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get("item_name")
        done = "done" in request.POST
        item.objects.create(name=name, done=done)

        return redirect("get_todo_list")
    return render(request, "todo/add_item.html")
