from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import *

# Create your views here.

def userlogin(request):
    if request.method=='POST':
        userrname=request.POST['userrname']
        password=request.POST['password']
        user=authenticate(request,userrname=userrname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request,'login.html')
def home(request):
    data=product.objects.all()
    return render(request,'home.html', {'data':data})
def logout_view(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method=='POST':
        userrname=request.POST['userrname']
        password=request.POST['password']
        email=request.POST['email']
        try:

            user=User.objects.create_user(username=userrname,password=password,email=email)
            user.save()

        except:
            return redirect('register')

        return redirect('login')
    else:
        return render(request,'register.html')
def viewproduct(request,pk):
 data=product.objects.filter(pk=pk)
 return render(request,'product.html',{'data':data})


