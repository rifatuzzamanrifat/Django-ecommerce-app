from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart, name='cart')
]
