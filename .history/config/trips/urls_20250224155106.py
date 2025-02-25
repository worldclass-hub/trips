from django.urls import path
from .views import home, find_guide, dashboard, add_to_cart, payment_method, success_page, coming_soon, about_us, pricing, services, view_more, blog, faqs, login, signUp, contact, icons, error_404

urlpatterns = [
    path('', home, name='home'),
    path('find_guide', find_guide, name='find_guide'),
    path('dashboard', dashboard, name='dashboard'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('payment_method', payment_method, name='payment_method'),
    path('coming_soon', coming_soon, name='coming_soon'),
    path('about_us', about_us, name='about_us'),
    path('pricing', pricing, name='pricing'),
    path('services', services, name='services'),
    path('success_page', success_page, name='success_page'),
    path('view_more', view_more, name='view_more'),
    
    path('blog', blog, name='blog'),
    path('faqs', faqs, name='faqs'),
    path('login', login, name='login'),
    path('signUp', signUp, name='signUp'),
    path('contact', contact, name='contact'),
    path('icons', icons, name='icons'),
    path('error_404', error_404, name='error_404'),
    
]
