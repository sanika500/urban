from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import *
from .forms import ProductForm


# Create your views here.

def userlogin(request):
    if 'username' in request.session:
        data=Product.objects.all()
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
     
        product = Product.objects.create(
        name=name,
        stock=stock,
        description=description,
        price=price,
        image=image,
        seller=request.user  )
        
       
        return redirect('sellerindex')
    
    return render(request, 'addproduct.html')  











    

        
            
         
            
        
        
        
    


