from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'index.html')

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            send = {
                'msg' : "user not found"
            }
            return render(request, 'signin.html', send)
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')

        user = User.objects.create_user(username = username,email = email, password = pass1, first_name = fname, last_name=lname)
        # user.first_name = fname
        # user.last_name = lname
        user.save()

        messages.success(request, f'{username} is created')

        return redirect('signin')
    return render(request, 'signup.html')