from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    # context is dict with all our items
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
    # context as a 3rd argument to render function
