from django.urls import path
from app import views
urlpatterns = [
   
    path('',views.homepage,name='home'),
    path('home/',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('product/',views.product,name='product'),
    path('productdetail/',views.productDetail,name='productdetail'),
    path('search/',views.search,name='search'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.register,name='register')
    
    
]