from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from TCSProj import settings
# Create your views here.
@login_required(login_url='/login/')


def Dashboard(request):
    return render(request, 'dashboard.html')