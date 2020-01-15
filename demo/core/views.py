from django.shortcuts import render
from .models import Order,OrderItem,Item
from django.views.generic import ListView,DetailView

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'
    context_object_name = 'items'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'

def checkout(request):
    return render(request,'checkout-page.html',{})

def product(request):
    return render(request,'product-page.html',{})


def itemlist(request):
    return render(request,'item_list.html',{})

