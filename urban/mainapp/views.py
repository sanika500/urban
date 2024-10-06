from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from urban.mainapp.models import product

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
    return render(request,'home.html')
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

def userhome(req):
    data=product.objects.all()
    product=product.objects.get(pk=pk)
    return render(req,'userhome.html',{'data':data})