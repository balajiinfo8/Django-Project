from django.urls import path 
from .views import ProductView

urlpatterns = [
    path("product/",ProductView,name='product-view')
]