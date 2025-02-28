from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import *
from .forms import ProductForm

import random
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm, OTPForm, ResetPasswordForm


# Create your views here.

def userlogin(request):
    if 'username' in request.session:
        data=Product.objects.all()
        return render(request,'home.html',{'data':data})
    
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=authenticate(request,username=username,password=password,email=email)
        if user is not None:
            login(request,user)
            request.session['username']= username
            return redirect('home')
        
    return render(request,'login.html')
def home(request):
    data=Product.objects.all()
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
 data=Product.objects.filter(pk=pk)
 return render(request,'product.html',{'data':data})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')




def seller(request):
    
    # confirmpassword=None
    
    if request.method=='POST':
        username=request.POST['sellername']
        password=request.POST['password']
        confirmpassword=request.POST['password']
        if not username or not password or not confirmpassword:
         messages.error(request,'all fields are required')
         
        elif confirmpassword != password: 
         messages.error(request,'password doesnot match')
         
        elif User.objects.filter(username=username).exists():
         messages.error(request,"username already exists")    
         
        else:   
         user=User.objects.create_user(username=username,password=password)
         user.is_staff=True
         user.save()
         return render(request,'seller.html')
    return render(request,'seller.html')
     
# def sellerlogin(request):
    # if 'username' in request.session:
    #     return redirect('sellerindex')
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     password=request.POST.get('password')
    #     # confirmpassword=request.POST.get('confirmpassword')
    #     user=authenticate(username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         request.session['username']= username
    #         return redirect('sellerindex')
    #         return render(request,"sellerlogin.html")
    #     return render(request, "sellerlogin.html", {'error': 'Invalid data'})
    # return render(request, "sellerlogin.html")



def sellerlogin(request):
    if 'username' in request.session:
        return redirect('sellerindex')  # Redirect to seller index page if already logged in.
    
    if request.method == 'POST':
        username = request.POST.get('sellername')  # Changed to match the form field name
        password = request.POST.get('password')   # Make sure it's 'password', not 'confirmpassword'
        
        user = authenticate(request, username=username, password=password)  # Properly authenticate
        if user is not None:
            login(request, user)  # Log in the user
            request.session['username'] = username  # Store the username in the session
            return redirect('sellerindex')  # Redirect to the seller index page after successful login
        
        return render(request, "sellerlogin.html", {'error': 'Invalid username or password'})  # Return error if authentication fails

    return render(request, "sellerlogin.html")  # Render the login page for GET request





    


# def sellerlogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('sellerindex')
#         else:
#             messages.error(request, "Invalid username or password.")

#     return render(request, 'sellerlogin.html')





# def sellerindex(request):
#     user = request.user
#     products = Product.objects.filter(seller=user)
#     return render(request, "sellerindex.html",{'products': products,'models':models})


# def sellerindex(request):

#     if request.user.is_authenticated and request.user.is_staff:
#         products = Product.objects.filter(seller=request.user)
        
#         return render(request, "sellerindex.html", {'products': products}) 
#     else:
       
#         return redirect('sellerlogin')




# def sellerindex(request):
   
#     products = Product.objects.all()

   
    

   
#     selected_model = request.POST.get('model', 'all')  
#     if selected_model != 'all':
       
#         products = products.filter(model__pk=selected_model)

   
#     context = {
#         'products': products,
#         'models': models
#     }

#     return render(request, 'sellerindex.html', context)



def sellerindex(request):
    user = request.user
    products = Product.objects.filter(seller=user)
   
    context = {
        'products': products,
      
    }
    return render(request, "sellerindex.html", context)





# def addproduct(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.seller = request.user  # Ensure the logged-in user is the seller
#             product.save()
#             return redirect('sellerindex')  # Redirect to seller index page after successful form submission
#     else:
#         form = ProductForm()
    
#     return render(request, 'addproduct.html', {'form': form})



def addproduct(request):
    if request.method == 'POST':
    
        name = request.POST['name']
        stock = request.POST['stock']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']  
     
        prod = Product.objects.create(
        name=name,
        stock=stock,
        description=description,
        price=price,
        image=image,
        bookingamount=5000,
        seller=request.user  )
        prod.save()
        
       
        return redirect('sellerindex')
    
    return render(request, 'addproduct.html')  



def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'edit_product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('sellerindex')

def contact(request):
    return  render(request,'contact.html')

def about(request):
    return render(request,"about.html")



otp_storage = {}

def generate_otp():
    """Generate a 6-digit OTP"""
    return str(random.randint(100000, 999999))

def request_otp(request):
    """Step 1: User enters email, OTP is sent"""
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                otp = generate_otp()
                otp_storage[email] = otp  # Store OTP temporarily
                send_mail(
                    "Password Reset OTP",
                    f"Your OTP for password reset is: {otp}",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                )
                request.session['email'] = email
                messages.success(request, "OTP sent to your email!")
                return redirect('verify_otp')
            except User.DoesNotExist:
                messages.error(request, "Email not registered!")
    else:
        form = EmailForm()
    return render(request, "forgot_password.html", {"form": form})

def verify_otp(request):
    """Step 2: User enters OTP"""
    email = request.session.get('email')
    if not email:
        return redirect('forgot_password')

    if request.method == "POST":
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            if otp_storage.get(email) == entered_otp:
                del otp_storage[email]  # Clear OTP after use
                messages.success(request, "OTP verified! Set a new password.")
                return redirect('reset_password')
            else:
                messages.error(request, "Invalid OTP!")
    else:
        form = OTPForm()
    return render(request, "verify_otp.html", {"form": form})

def reset_password(request):
    """Step 3: User resets password"""
    email = request.session.get('email')
    if not email:
        return redirect('forgot_password')

    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            if new_password == confirm_password:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password reset successful! You can now log in.")
                return redirect('login')
            else:
                messages.error(request, "Passwords do not match!")
    else:
        form = ResetPasswordForm()
    return render(request, "reset_password.html", {"form": form})







    

        
            
         
            
        
        
        
    


