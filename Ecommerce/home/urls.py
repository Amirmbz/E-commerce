from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/cart', views.cart, name='cart'),
    path('/about', views.about, name='about'),
    path('/shop', views.shop, name='shop'),
    path('/contact', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
]
