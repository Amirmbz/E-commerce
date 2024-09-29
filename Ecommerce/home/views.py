from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from secrets import token_hex


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


def checkout(request):
    return render(request, 'home/checkout.html')


def shop_single(request):
    return render(request, 'home/shop-single.html')


def thankyou(request):
    return render(request, 'home/thankyou.html')


def register(request):

    logout(request)
    request.session.clear()

    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username or not password:
        return render(request, "home/thankyou.html", {
            "text": "enter username and password",
            "nogood": "true"
        })

    elif request.POST.get("confirmation") != password:
        return render(request, "home/thankyou.html", {
            "text": "password and confirmation didn't match",
            "nogood": "true"
        })

    if User.objects.filter(username=username).exists():
        return render(request, "home/thankyou.html", {
            "text": "Username is already taken.",
            "nogood": "true"
        })

    user = User.objects.create(
        username=username,
        password=make_password(password)
        )
    user.save()

    login(request, user)

    return render(request, 'home/authentication.html')


def signin(request):

    logout(request)
    request.session.clear()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, 'home/thankyou.html', {
                "text": "enter username and password",
                "nogood": "true"
            })

        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)

            return redirect('index')

        return render(request, 'home/thankyou.html', {
            "text": "username and/or password is incorrect",
            "nogood": "true"
        })

    return render(request, 'home/login.html')


def authentication(request):

    if request.method == "POST":

        email = request.POST.get("email")

        if not email:
            return render(request, 'home/thankyou.html', {
                "text": "enter email",
                "nogood": "true"
            })

        request.session['email'] = email

        otp = token_hex(3)
        send_mail(
            'Your Verification Code',
            f'Your verification code is {otp}',
            'fortestamb@gmail.com',
            [email],
            fail_silently=False,
        )
        request.session['otp'] = otp

        return render(request, 'home/verification.html')

    return render(request, 'home/authentication.html')


def verification(request):
    if request.method == "POST":

        otp = request.POST.get("otp")

        if not otp:
            return render(request, 'home/thankyou.html', {
                "text": "enter one time password",
                "nogood": "true"
            })

        if otp == request.session.get('otp'):
            user = request.user
            user.email = request.session.get('email')
            user.save()

            del request.session['otp']
            del request.session['email']
            return render(request, 'home/thankyou.html', {
                "text": "enter one time password",
                "nogood": "true"
            })

        return render(request, 'home/thankyou.html', {
            "text": "enter one time password",
            "nogood": "true"
        })

    return render(request, 'home/verification.html')
