# from django.shortcuts import render , redirect
# from .models import Product
# from django.http import HttpResponse 
# from .forms import ProductForm

# # Create your views here.
# def ProductView(request):
#     product = Product.objects.all()
#     return render(request , 'home.html',{'product' : product})

# # user can display their product 
# def UploadProduct(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return  redirect('product-View') # redirect to display new product
#         else:
#             form = ProductForm() # retrun the form to render

#         return render(request,'upload_product.html',{'form':form})


# from django.shortcuts import render, redirect , get_list_or_404 , get_object_or_404
# from .models import Product
# from .forms import ProductForm

# # Home page: display all products
# def ProductView(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', {'product': products})

# # Upload page: handle product form
# def UploadProduct(request,pk):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product-view')  # ✅ Must match name in urls.py
#     else:
#         form = ProductForm()  # ✅ Handles GET request

#     return render(request, 'upload_product.html', {'form': form})  # ✅ Always return a response


# # Update existing product
# def ProductEdit(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     form = ProductForm(request.POST or None, request.FILES or None, instance=product)

#     if form.is_valid():
#         form.save()
#         return redirect('product-view')  # Redirect to homepage or detail view

#     return render(request, 'update_product.html', {'form': form})

# # delete existing data from website 
# def DeleteProduct(request,pk):
#     Product = get_object_or_404(Product,pk=pk)
#     Product.delete()
#     return redirect('product-view')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Home page: display all products
def ProductView(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Upload page: handle product form
def UploadProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-view')
    else:
        form = ProductForm()
    return render(request, "upload_product.html", {'form': form})

# View single product details
def ProductDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Update existing product
def ProductEdit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product-view')
    return render(request, 'update_product.html', {'form': form})

# Delete product
def DeleteProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product-view')

# blog website 
# views.py
from django.shortcuts import render
from .models import BlogPost

# blog list
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

# Blog detail 
def blog_detail(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    return render(request,'blog_detail.html',{'post':post})

