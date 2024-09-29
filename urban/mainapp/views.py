from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method=='POST':
        userrname=request.POST['userrname']
        password=request.POST['password']
        user=authenticate(request,userrname=userrname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def logout_view(request):
    logout(request)
    return redirect('index')
def register(request):
    if request.method=='POST':
        userrname=request.POST['userrname']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(userrname=userrname,password=password,email=email)
        user.save()
        return redirect('login')
    else:
        return render(request,'register.html')
