from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all() # entering records
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
    else:    #passing to html page
        return render(request, 'home.html', {'records':records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # auth and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"You have Successfully Registered!")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form })
        
    return render(request, 'register.html', {'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        # look
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request,"You must be Logged in to View that Page.")
        return redirect('home')


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request,"You must be Logged in to DELETE a record.")
        return redirect('home')
