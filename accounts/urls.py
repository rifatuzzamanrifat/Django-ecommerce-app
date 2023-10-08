from django.urls import path
from .views import login, signup, forget_pass, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', signup, name='logout'),
    path('forget_pass/', forget_pass, name='forget_pass')
]
