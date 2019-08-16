from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, ListView
from braces.views import SelectRelatedMixin
from django.urls import reverse
from shop.models import Vegtables
from cart.models import Wishlist

class CartPage(TemplateView):
    template_name = 'cart.html'

class WhishlistPage(ListView):
    model = Wishlist
    template_name = 'wishlist.html'

# class ThanksPage(TemplateView):
#     del request.session['cart']
#     template_name = 'thanks.html'

def ThanksPage(request):
    if 'cart' in request.session:
        del request.session['cart']
    return render(request,'thanks.html')
    
def view_cart(request):
    vegtable = Vegtables.objects.all
    args = {'vegtable':vegtable}
    return render(request,'cart.html',args)

def add_to_cart(request, pk=None, qnt=None):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    if pk:
        if qnt:
            cart = request.session.get('cart', {})
            if not pk in cart:
                cart[pk] = qnt
            else:
                cart[pk] = int(cart[pk]) + int(qnt)
                
            request.session['cart'] = cart

            vegtable = Vegtables.objects.all
            args = {'vegtable':vegtable, 'pk':pk}
            return render(request,'single_product.html',args)
        else:
            return render(request,'shop.html')
    else:
        return render(request,'shop.html')

# def remove_from_cart(request, pk=None):
#     if 'cart' in request.session and pk:
#         cart_dict = request.session['cart']
#         print(cart_dict)
#         del cart_dict[pk]
#         request.session['cart'] = cart_dict
#         print(cart_dict)

#     return render(request,'cart.html')

class add_one_to_cart(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        pg = self.kwargs.get("pg")
        red_url = "shop:shop"
        if pg == "1":
            red_url = "home"
        elif pg == "2":
            red_url = "shop:shop"
        elif pg == "3":
            red_url = "shop:single_product"
            
        return reverse(red_url)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        if pk:
            cart = request.session.get('cart', {})
            if not pk in cart:
                cart[pk] = 1
            else:
                cart[pk] = int(cart[pk]) + 1
                    
            request.session['cart'] = cart

        return super().get(request, *args, **kwargs)

class remove_from_cart(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("cart:cart")

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        if 'cart' in request.session and pk:
            cart_dict = request.session['cart']
            del cart_dict[pk]
            request.session['cart'] = cart_dict

        return super().get(request, *args, **kwargs)

class add_to_wishlist(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        pg = self.kwargs.get("pg")
        red_url = "shop:shop"
        if pg == "1":
            red_url = "home"
        elif pg == "2":
            red_url = "shop:shop"
        elif pg == "3":
            red_url = "shop:single_product"
        elif pg == "4":
            red_url = "cart:wishlist"
                        
        return reverse(red_url)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        try:
            print(Wishlist.objects.get(user=request.user, vegtable=Vegtables.objects.get(pk=pk)))
            if Wishlist.objects.filter(user=request.user, vegtable=Vegtables.objects.get(pk=pk), wish=True):
                Wishlist.objects.filter(user=request.user, vegtable=Vegtables.objects.get(pk=pk), wish=True).update(wish=False)
            else:
                Wishlist.objects.filter(user=request.user, vegtable=Vegtables.objects.get(pk=pk), wish=False).update(wish=True)
        except:
            temp_wish = Wishlist.objects.get_or_create(user=request.user, vegtable=Vegtables.objects.get(pk=pk), wish=True)[0]
            temp_wish.save()

        return super().get(request, *args, **kwargs)