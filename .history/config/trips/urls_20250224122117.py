from django.urls import path
from .views import home, find_guide

urlpatterns = [
    path('', home, name='home'),
    path('find_guide', find_guide, name='find_guide'),
]
