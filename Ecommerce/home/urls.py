from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop-single/', views.shop_single, name='shop_single'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('login/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('authentication/', views.authentication, name='authentication'),
    path('verification/', views.verification, name='verification')
]
