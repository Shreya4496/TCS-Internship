from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from TCSProj import settings
from django.http import HttpResponse
from .forms import UserForm,ServiceProvider,Customer

from ComplaintsForum.models import Chat



def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                Chat.objects.all().delete()
                return render(request, 'chat/home.html')
            else:
                return render(request, 'chat/home.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'chat/login.html', {'error_message': 'Invalid login'})
    return render(request, 'chat/login.html')





def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        option=form.cleaned_data['role']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password, email=email)
        if option=='provider':
            form = ServiceProvider(request.POST)
            data = form.save(commit=False)
            data.save()
        elif option=='customer':
            form = Customer(request.POST)
            data = form.save(commit=False)
            data.save()

        if user is not None: 
            if user.is_active:
                #login(request, user)
                q=1
                return render(request,'chat/home.html', {'q': q})
        return render(request,'chat/home.html', {'q': q})


    context ={
        "form": form,
    }
    return render(request, 'chat/registration_form.html', context)



"""

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "chat/login.html", {'next': next})
"""
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def Home(request):
    c = Chat.objects.all()
    return render(request, "chat/home.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'chat/messages.html', {'chat': c})

