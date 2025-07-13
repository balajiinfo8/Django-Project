from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = { 
            'item_list' : item_list,
    }
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse('This is a item view')

# own views 
def detail(request,pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item' : item, # item same define in the html : 9 to 11
    }
    return render(request,'food/details.html',context)