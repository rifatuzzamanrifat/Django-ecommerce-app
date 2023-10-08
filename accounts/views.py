from django.shortcuts import render


# Create your views here.
def forget_pass(r):
    return render(r, 'accounts/forget_pass.html')


def signup(r):
    return render(r, 'accounts/signup.html')


def login(r):
    return render(r, 'accounts/login.html')
