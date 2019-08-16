from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.http import Http404
from shop.models import Vegtables
from cart.models import Wishlist
from . import models

# class ShopPage(ListView):
#     model = Vegtables
#     template_name = 'shop.html'

# class SingleProduct(ListView):
#     model = Vegtables
#     template_name = 'single_product.html'

def ShopPage(request):
    vegtable = Vegtables.objects.all
    wishlist = Wishlist.objects.all
    args = {'vegtable':vegtable, 'wishlist':wishlist}
    return render(request,'shop.html',args)

def SingleProduct(request, pk=None):
    wishlist = Wishlist.objects.all
    if pk:
        vegtable = Vegtables.objects.all
        args = {'vegtable':vegtable, 'pk':pk, 'wishlist':wishlist}
        return render(request,'single_product.html',args)

    else:
        args = {'wishlist':wishlist}
        return render(request,'shop.html',args)