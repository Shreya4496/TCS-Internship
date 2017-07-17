
# Create your views here.
from django.shortcuts import render, redirect, render_to_response
from .forms import SLAForm,ServiceSelect,ServiceCreate
# from django.views.generic import View
# from django.contrib import messages
from ComplaintsForum.models import Service
def service_new(request):
    if request.method == "POST":
        form = ServiceSelect(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.username = request.session.get('username')
            data.save()
            return render(request, 'done.html')
    else:
        form = ServiceSelect()
    return render(request, 'sla.html', {'form': form})

def sla_new(request):
    if request.method == "POST":
        form = SLAForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.username = request.session.get('username')
            data.save()
            return render(request, 'done.html')
    else:
        form = SLAForm()
    return render(request, 'sla_new.html', {'form': form})

def service_create(request):
    if request.method == "POST":
        form = ServiceCreate(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.username = request.session.get('username')
            data.save()
            return render(request, 'done.html')
    else:
        form = ServiceCreate()
    return render(request, 'service_create.html', {'form': form})

def service_all(request):
    posts = Service.objects.all()
    print (posts)
    return render(request, "list.html", {'posts': posts})