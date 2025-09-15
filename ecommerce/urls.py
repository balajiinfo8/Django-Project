# from django.urls import path 
# from .views import ProductView , UploadProduct , ProductEdit , DeleteProduct

# urlpatterns = [
#     # display product
#     path("",ProductView,name='product-view'),
#     # upload new product 
#     path("upload/",UploadProduct,name='upload-product'),
#     # update existing product
#     path('update/<int:pk>',ProductEdit,name='update-product'),
#     # delete existing product
#     path('product/<int:pk',DeleteProduct,name='delete-product'),
# ]

from django.urls import path
from .views import (
    ProductView,
    UploadProduct,
    ProductDetail,
    ProductEdit,
    DeleteProduct
)
from . import views

urlpatterns = [
    # Home page: list all products
    path("", ProductView, name='product-view'),

    # Upload new product
    path("upload/", UploadProduct, name='upload-product'),

    # View single product details
    path("product/<int:pk>/", ProductDetail, name='product-detail'),

    # Update existing product
    path("update/<int:pk>/", ProductEdit, name='update-product'),

    # Delete product
    path("delete/<int:pk>/", DeleteProduct, name='delete-product'),

    # blog website 
    path('blog/',views.blog_list,name='blog-list'),
    # count blog list 
    path('blog/<int:pk>/',views.blog_detail,name='blog-detail')
]
