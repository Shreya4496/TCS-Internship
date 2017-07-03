
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from TCSProj import settings
# Create your views here.
def Dashboard(request):
    return render(request, 'base.html')