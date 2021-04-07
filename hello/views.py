from django.shortcuts import render
from django.template import RequestContext

from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from web_project import settings
#import time 
from .models import Chat



def intro(request):
    
    # return response with template and context 
    return render(request, "intro.html")
def homepage(request):
    
    # return response with template and context 
    return render(request, "homepage.html")
def register(request):
    
    # return response with template and context 
    return render(request, "register.html")
def members(request):
    
    # return response with template and context 
    return render(request, "members.html")
def bot(request):
    
    # return response with template and context 
    return render(request, "bot.html")
def contact(request):
    
    # return response with template and context 
    return render(request, "contact.html")
def about(request):
    
    # return response with template and context 
    return render(request, "about.html")
def test(request):
    return render(request,'test.html',{'next': next})

def index(request):
    #return render_to_response('index.html')
    return render(request, 'login.html', {'next': next})

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                #WelcomeUser(user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "login.html", {'next': next})

def Logout(request):
    #logout(request)
    Chat.objects.all().delete()
    return HttpResponseRedirect('/login/')

def Home(request):
    c = Chat.objects.all()
    return render(request, "home.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        
        c = Chat(user=request.user, message=msg)

        #if(msg[0:6] == "Robot:"):
        callRobot(msg, request)
            
        
        msg = c.user.username+": "+msg

        c = Chat(user=request.user, message=msg)

        if msg != '':            
            c.save()
        #mg = src="https://scontent-ord1-1.xx.fbcdn.net/hprofile-xaf1/v/t1.0-1/p160x160/11070096_10204126647988048_6580328996672664529_n.jpg?oh=f9b916e359cd7de9871d8d8e0a269e3d&oe=576F6F12"
        return JsonResponse({ 'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})

