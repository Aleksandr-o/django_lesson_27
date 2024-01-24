from django.contrib.auth.models import User
from django.shortcuts import render

from apps.todo.forms import CreateTaskForm
from apps.todo.models import (
    Task,
    Category,
    Status
)

# Create your views here.
def home_page(request):
    return render(
        request=request,
        template_name='main.html'
    )

def get_all_tasks(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }

    return render(
        request=request,
        template_name='todo/all_tasks.html',
        context=context
    )

def create_new_task(request):
    users = User.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()

    if request.metod == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task_data = form.cleaned_data
            Task.objects.create(**task_data)