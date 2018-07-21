from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

# the index function is called when root is visited
def index(request):
	return render(request, 'index.html', { 'courses': Course.objects.all() })

def course_add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')

def remove(request, id):
    return render(request, 'remove.html', { "courses": Course.objects.get(id=id) })

def destroy(request, id):
    d = Course.objects.get(id=id)
    d.delete()
    return redirect('/')
