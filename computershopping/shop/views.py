from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import CartItem
# Create your views here.

def home(request):
    # products = Product.objects.all()
    return render(request, 'template/shop/home.html')

