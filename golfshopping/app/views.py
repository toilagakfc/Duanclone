from django.shortcuts import render,redirect
from .models import Category



def homepage(request):
    categoryList = Category.objects.filter(parent__isnull=True,status='Active').values()
    subcategoryList = Category.objects.filter(parent__isnull=False,status='Active').values()
    context = {"categoryList":categoryList,
               "subcategoryList":subcategoryList}
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