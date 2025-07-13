from django.urls import path , include 
from . import views

urlpatterns = [
    path('', views.index , name='index/'),
    path('item/',views.item,name='item/'),
    path('own/',views.ownview,name='ownviews')
]
