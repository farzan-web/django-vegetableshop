from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'shop'

urlpatterns = [
    path('', views.ShopPage, name='shop'),
    # path('single_product/', views.ShopPage.as_view(), name='single_product'),
    url(r"single_product/(?P<pk>\d+)/$",views.SingleProduct,name="single_product"),
]
