from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import *

# Create your views here.

def userlogin(request):
    if 'username' in request.session:
        data=product.objects.all()
        return render(request,'home.html',{'data':data})
    
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['username']= username
            return redirect('home')
        
    return render(request,'login.html')
def home(request):
    data=product.objects.all()
    return render(request,'home.html', {'data':data})
def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        try:

            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()

        except:
            return redirect('register')

        return redirect('login')
    else:
        return render(request,'register.html')
def viewproduct(request,pk):
 data=product.objects.filter(pk=pk)
 return render(request,'product.html',{'data':data})

def seller(request):
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST[' confirm password']
        if not username or not password or not confirmpassword:
         messages.error(request,'all fields are required')
         
     elif confirmpassword !="password": 
         messages.error(request,'password doesnot match')
         
     elif User.objects.filter(username=username).exists():
         messages.error(request,"username already exists")    
         
     else:   
         user=User.objects.createseller(username=username,password=password)
         user.is_staff=True
         user.save()
         return render(request,'seller.html')
         
            
        
        
        
    


