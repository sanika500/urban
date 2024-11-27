from django.urls import path
from.import views 
urlpatterns=[
     path('register',views.register,name="register"),
     path('home',views.home,name="home"),
     path('',views.userlogin,name="login"),
     path('viewproduct/<pk>/',views.viewproduct,name="viewproduct"),
     path('seller/',views.seller,name="seller"),
     path('sellerlogin',views.sellerlogin,name="sellerlogin"),
     path('sellerindex',views.sellerindex,name="sellerindex"),
     path('login',views.login_view,name="login"),
     path('addproduct/', views.addproduct, name='addproduct'),
     path('edit/<int:pk>/', views.edit_product, name='edit'),
     path('delete/<int:pk>/', views.delete_product, name='delete'),
    
]