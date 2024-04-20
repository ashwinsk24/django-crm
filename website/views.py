from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check auth
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #auth
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"There was an error logging in. Please try again.")
            return redirect('home')
    else:    
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})

