from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    # path('', views.CartPage.as_view(), name='cart'),
    path('', views.view_cart, name='cart'),
    url(r"add/(?P<pk>\d+)(?P<qnt>\d+)/$",views.add_to_cart,name="add_to_cart"),
    path('wishlist/', views.WhishlistPage.as_view(), name='wishlist'),
    path('thanks/', views.ThanksPage, name='thanks'),
    url(r"remove/(?P<pk>\d+)/$",views.remove_from_cart.as_view(),name="remove"),
    url(r"addone/(?P<pk>\d+)/(?P<pg>\d+)/$",views.add_one_to_cart.as_view(),name="addone"),
    url(r"addwish/(?P<pk>\d+)/(?P<pg>\d+)/$",views.add_to_wishlist.as_view(),name="addwish"),
]
