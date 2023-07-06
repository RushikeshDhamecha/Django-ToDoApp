from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Task


# Create your views here.
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title') #get('title'): title value from html page
        desc = request.POST.get('desc')  #get('desc'): desc value from html page
        if title and desc:
            instance = Task(addTitle=title, addDesc=desc)
            instance.save()
            messages.success(request, 'Task added successfully')
        elif title:
            messages.success(request, 'Description is missing')
            # messages.add_message(request, messages.SUCCESS, 'Desc is missing')
        elif desc:
            messages.success(request, 'Title is missing')
    return render(request, 'index.html')


def list_task(request):
    if request.method == 'POST':
        chkbox = request.POST.getlist('chkbox')  #get('chkbox'): chkbox value from html page
        if chkbox:
            Task.objects.filter(id__in=chkbox).delete() #id__in allows you to filter task objects based on a list of IDs, basically if you have to get more than one id
    tasks = Task.objects.all()
    return render(request, 'list.html', {'tasks': tasks})


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)  # to retrieve the value of particular id
    if request.method == 'POST':
        edited_title = request.POST.get('title')  # get access the value of title text box
        edited_desc_lines = request.POST.getlist('desc')
        edited_desc = ''.join(edited_desc_lines)  # Join the description lines into a single string

        task.addTitle = edited_title  # store task[(current object) dot its title/desc] to new title(edited_title)
        task.addDesc = edited_desc
        task.save()
        return redirect('list')
    context = {
        'task': task
    }
    return render(request, 'edit.html', context)
