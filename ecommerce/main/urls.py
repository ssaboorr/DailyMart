from django.urls import path
from main import views

urlpatterns = [
    path('home/',views.home,name='homepage'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('cart/',views.cart,name='cart'),
    path('product_details/',views.product_detail,name='product_details'),
    path('categories/',views.categories,name='categories'),
    path('profile/',views.profile,name='profile'),
    path('settings/',views.setting,name='settings'),
    path('orders/',views.orders,name='orders'),




]
