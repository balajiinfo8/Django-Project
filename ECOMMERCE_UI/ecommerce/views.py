from django.shortcuts import render
from .models import Product

# Create your views here.
def ProductView(request):
    product = Product.objects.all()
    return render(request , 'home.html',{'product' : product})
