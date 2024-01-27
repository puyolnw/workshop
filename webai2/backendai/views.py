from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def homepage(request):
    return HttpResponse("HELLO WELCOME")

def pageuser(request):
    return HttpResponse("<h1>AYO USER</h1>")

def pageinfo(request):
    return HttpResponse ('<h1 style="text-align: center; font-size: calc(5 * 1em);">THIS IS PAGEINFO</h1/n><h1 style="text-align: center; font-size: calc(2 * 1em);">SATURDAY</h1/n>')


def pageuserinfo(request,username):
    return HttpResponse(f'<h1 style="text-align: center; font-size: calc(5 * 1em);">THIS IS PAGEUSER</h1/n><h1 style="text-align: center; font-size: calc(2 * 1em);">WELCOME {username}</h1/n>')

def backendpage(request):
    context = {}
    return render(request,'backendpage.html',context)

def registerpage(request):
    context = {}
    return render(request,'register.html',context)

def registercreate(request):
    if request.method == "POST":
        firstnameinput = request.POST.get('firstname', None)
        lastnameinput = request.POST.get('lastname', None)
        emailinput = request.POST.get('email', None)
        passwordinput = request.POST.get('password', None)

        if firstnameinput is not None and lastnameinput is not None and emailinput is not None and passwordinput is not None:
            checkuser = User.objects.filter(username=emailinput).count()
            if checkuser == 0:
                createuser = User.objects.create_user(username=emailinput, email=emailinput, password=passwordinput)
                createuser.first_name = firstnameinput
                createuser.last_name = lastnameinput
                createuser.save()

                if createuser:
                    messages.success(request, "Registration successful. You can now log in.")
                    return redirect(registerpage)
                else:
                    messages.error(request, "An error occurred. Please try registering again.")
                    return redirect(registerpage)
            else:
                messages.error(request, "Username already exists. Please choose a different one.")
                return redirect(registerpage)
        else:
            messages.error(request, "Please fill in all the required fields.")
            return redirect(registerpage)
    else:
        messages.error(request, "An error occurred. Please try registering again.")
        return redirect(registerpage)
    

def loginpage(request):
    context = {}
    return render(request,'login.html',context)
    
def loginaction(request):
    if request.method == "POST":
        emailinput = request.POST.get('email', None)
        passwordinput = request.POST.get('password', None)
        if emailinput is not None and passwordinput is not None:
            usercheck = authenticate(username=emailinput, password=passwordinput)
            if usercheck:
                login(request, usercheck)
                messages.success(request, "Successfully logged in")
                return redirect(backendpage)
            else:
                messages.error(request, "Invalid username or password. Please try again.")
                return redirect(loginpage)
        else:
            messages.error(request, "Please fill in all the required fields.")
            return redirect(loginpage)
    else:
        messages.error(request, "An error occurred. Please try again.")
        return redirect(loginpage)
# Create your views here.
