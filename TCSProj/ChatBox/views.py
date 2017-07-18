from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from TCSProj import settings
from django.http import HttpResponse
from .forms import UserForm,ServiceProvider,Customer
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import get_object_or_404
from ComplaintsForum.models import Chat



def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        u= User.objects.all().order_by('?')[:5]

        context = {
            'u' : u
        }
        if user is not None:
            if user.is_active:
                login(request, user)
                Chat.objects.all().delete()
                return render(request, 'chat/pop.html')
            else:
                return render(request, 'chat/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'chat/login.html', {'error_message': 'Invalid login'})
    return render(request, 'chat/login.html')

#CHANGE PASSWORD
def privacy(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return render(request,'dashboard.html')
        return render(request,'dashboard.html')
    else :
        form = PasswordChangeForm(user=request.user)
        context ={
        "form": form,
        }
        return render(request,'privacy_settings.html',context)


"""
def search(request):
    u = User.objects.all()
    query=request.GET.get("q")
    if query:
        u = u.filter(
            Q(username__icontains=query)|
            Q(email__icontains=query)
            ).distinct()
    return render(request, 'dashboard.html', {'u': u})

"""




def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password, email=email)
        if user is not None:
            user.is_active = False
            user.save()
            id = user.id
            email = user.email
            send_email(email, id)
                #return render(request, 'thankyou.html')
            #if user.is_active:
                #login(request, user)
            q=1
            return render(request,'chat/after_reg.html',{'q': q})
            #return render(request,'chat/after_reg.html',{'q': q})
        return render(request,'chat/after_reg.html',{'q': q})


    context ={
        "form": form,
    }
    return render(request, 'chat/registration_form.html', context)
def send_email(toaddr,id):
	text = "Hi!\nHow are you?\nHere is the link to activate your account:\nhttp://127.0.0.1:8000/register_activate/activation/?id=%s" %(id)
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	msg = MIMEMultipart('alternative')
	msg.attach(part1)
	subject="Activate your account at SealDeal"
	msg="""\From: %s\nTo: %s\nSubject: %s\n\n%s""" %("sealdeal16@gmail.com",toaddr,subject,msg.as_string())
	#Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
	#https://www.google.com/settings/security/lesssecureapps
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login("sealdeal16@gmail.com","tcsproject")
	server.sendmail("sealdeal16@gmail.com",[toaddr],msg)
	server.quit()

def activate(request):
	id=int(request.GET.get('id'))
	user = User.objects.get(id=id)
	user.is_active=True
	user.save()
	return render(request,'activation.html')

def choosen_role(request):
    q1 = request.GET.get("chooseone")
    if q1=="provider":
        bit=0
        form = ServiceProvider(request.POST)
        data = form.save(commit=False)
        data.save()
    elif q1=="client":
        bit=1
        form = Customer(request.POST)
        data = form.save(commit=False)
        data.save()
    return redirect(request,'dashboard.html',{'bit':bit})




"""
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
                return render(request,'dashboard.html', {'q': q})
        return render(request,'dashboard.html', {'q': q})


    context ={
        "form": form,
    }
    return render(request, 'chat/registration_form.html', context)

"""

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
  #  return render(request, "homepage.html")
    return HttpResponseRedirect('/homepage/')

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



