from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def cart(request):
    return render(request, 'home/cart.html')


def about(request):
    return render(request, 'home/about.html')


def shop(request):
    return render(request, 'home/shop.html')


def contact(request):
    return render(request, 'home/contact.html')
