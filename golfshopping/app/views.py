from django.shortcuts import render,redirect
from .models import *



def homepage(request):
    # categoryList = Category.objects.filter(parent__isnull=True,status='Active').values()
    categoryList = Category.objects.filter(parent__isnull=True,status='1').values()
    subcategoryList = Category.objects.filter(parent__isnull=False,status='1').values()
    products = Products.objects.filter(isHot=1).values()
    context = {"categoryList":categoryList,
               "subcategoryList":subcategoryList,
               "products":products
               }
    return render(request,'app/homePage.html',context)

def about(request):
    return render(request,'app/pageAbout.html')

def news(request):
    return render(request,'app/pageNews.html')

def contact(request):
    return render(request,'app/contact.html')

def search(request):
    return render(request, 'app/searchPage.html')

def product(request):
    return render(request,'app/product.html')

def productDetail(request):
    return render(request,'app/productDetail.html')

def loginPage(request):
    return render(request,'app/loginPage.html')

def register(request):
    return render(request,'app/registerPage.html')