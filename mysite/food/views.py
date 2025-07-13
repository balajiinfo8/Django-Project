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
    return HttpResponse("This is ID no/id : %s " % pk)