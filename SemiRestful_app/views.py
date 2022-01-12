from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages

from .models import *

# Create your views here.
def index(request):
    context = {
        'all_shows': TV_show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = TV_show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/new')
    else:
        if request.method == 'POST':
            print(request.POST)
            TV_show.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                description = request.POST['description']
            )
            return redirect('/')


def show(request, id):
    one_show = TV_show.objects.get(id = id)
    context = {
        'show' : one_show 
    }
    print(context['show'])
    return render(request, 'show.html', context)

def edit(request, id):
    one_show = TV_show.objects.get(id = id)
    context = {
        'show' : one_show
    }
    return render(request, 'edit.html', context)

def update(request, id):
    # errors = TV_show.objects.validator(request.POST)
    # if errors:
    #     for key, value in errors.items():
    #         messages.error(request, value) 
    #     return redirect('/edit')

    update= TV_show.objects.get(id = id)
    update.title = request.POST['title']
    update.network = request.POST['network']
    update.release_date = request.POST['release_date']
    update.description = request.POST['description']
    update.save()
    return redirect('/')

def delete(request, id):
    show_to_delete = TV_show.objects.get(id = id)
    show_to_delete.delete()
    return redirect('/')