from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def user_login(request):
    return render(request, 'main/login.html')


def user_signup(request):
    return render(request, 'main/signup.html')


def cart(request):
    return render(request, 'main/cart.html')


def product_detail(request):
    return render(request, 'main/product_detail.html')


def categories(request):
    return render(request, 'main/categories.html')


def profile(request):
    return render(request, 'main/profile.html')


def orders(request):
    return render(request, 'main/orders.html')


def setting(request):
    return render(request, 'main/setting.html')


def logout(request):
    return render(request, 'main/login.html')
