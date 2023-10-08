from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def forget_pass(r):
    return render(r, 'accounts/forget_pass.html')


def signup(r):
    if r.method == 'POST':
        name = r.POST.get('name')
        username = r.POST.get('username')
        email = r.POST.get(' email ')
        password = r.POST.get(' pass')
        if len(password) < 8:
            messages.warning(r, "Password must be 8 character.")
        else:
            if password:
                a = []
                b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                c = []
                d = ['!', '@', '#', '$', '&', '*', '/', '_', '-']
                for i in b:
                    if i in password:
                        a.append(i)
                for i in d:
                    if i in password:
                        c.append(i)
                    if len(a) != 0 and len(c) != 0:
                        if password == password:
                            if User.objects.filter(username=username).exits():
                                messages.warning(r, "Username is Already Taken.")
                            elif User.objects.filter(email=email).exits():
                                messages.warning(r, "Email is Already Taken.")
                            else:
                                user = User.objects.create_user(name=name, username=username, email=email,
                                                                password=password)
                                user.set_password(password)
                                user.save()
                                messages.success(r, "Profile Created.")
                                return redirect('Log In')
                        else:
                            messages.warning(r, "Password not Matched.")
                    else:
                        messages.warning(r, "Enter minimum 1 number and 1 special character in your password.")

    return render(r, 'accounts/signup.html')


def login(r):
    if r.user.is_authenticated:
        return redirect('home')
    if r.method == 'POST':
        username = r.POST.get('name')
        password = r.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(r, user)
            messages.warning(r, "User Logged In.")
            return redirect('home')
        else:
            messages.warning(r, "User Not Found.")
            return redirect('signup')
    return render(r, 'accounts/login.html')


def logout(r):
    auth.logout(r)
    return redirect('login')
