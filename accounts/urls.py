from django.urls import path
from .views import forget_pass, signup, login

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('forget_pass/', forget_pass, name='forget_pass')
]
