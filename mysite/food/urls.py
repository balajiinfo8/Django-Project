from django.urls import path , include 
from . import views

urlpatterns = [
    # /food/ 
    path('', views.index , name='index/'),
    # /food/item/
    path('item/',views.item,name='item/'),
    # /food/1 
    path("<int:pk>/",views.detail,name='details'),

    path('own/',views.detail,name='ownviews')
]
