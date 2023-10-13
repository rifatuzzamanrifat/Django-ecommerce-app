from django.urls import path
from .views import login, signup, forget_pass, logout, verify_otp

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('forget_pass/', forget_pass, name='forget_pass'),
    path('verify_otp/', verify_otp, name='verify_otp')
]
