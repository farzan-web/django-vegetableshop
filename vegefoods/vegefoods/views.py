from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from shop.models import Vegtables
from cart.models import Wishlist

# class HomePage(ListView):
#     model = Vegtables
#     template_name = 'index.html'

def HomePage(request):
    vegtable = Vegtables.objects.all
    wishlist = Wishlist.objects.all
    args = {'vegtable':vegtable, 'wishlist':wishlist}
    return render(request,'index.html',args)

class AboutPage(TemplateView):
    template_name = 'about.html'

class checkoutPage(TemplateView):
    template_name = 'checkout.html'

class contactPage(TemplateView):
    template_name = 'contact.html'
            