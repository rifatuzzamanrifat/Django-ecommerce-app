from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth import update_session_auth_hash


# Create your views here.


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        password2 = request.POST.get('pass2')
        if len(password) < 8:
            messages.warning(request, "Password must be 8 character.")
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
                        if password == password2:
                            if User.objects.filter(username=username).exists():
                                messages.warning(request, "Username is Already Taken.")
                            elif User.objects.filter(email=email).exists():
                                messages.warning(request, "Email is Already Taken.")
                            else:
                                user = User.objects.create_user(first_name=name, username=username, email=email,
                                                                password=password)
                                user.set_password(password)
                                user.save()
                                messages.success(request, "Profile Created.")
                            return redirect('login')
                        else:
                            messages.warning(request, "Password not Matched.")
            else:
                messages.warning(request, "Enter minimum 1 number and 1 special character in your password.")

    return render(request, 'accounts/signup.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.warning(request, "User Logged In.")
            return redirect('home')
        else:
            messages.warning(request, "User Not Found.")
            return redirect('signup')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def forget_pass(request):
    otp = random.randint(1111, 9999)
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            if email:
                send_mail_registration(email, otp)
                username = User.objects.get(email=email)
                if username:
                    try:
                        prof = Profile.objects.get(username=username)
                        if prof:
                            prof.otp = otp
                            prof.save()
                            return redirect('verify_otp')
                    except:
                        prof = Profile.objects.create(username=username, otp=otp)
                        prof.save()
                        return redirect('verify_otp')
        except:
            messages.warning(request, "User Not Found.")
            return redirect('forget_pass')

    return render(request, 'accounts/forget_pass.html')


def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        otp = request.POST.get('otp')
        if email:
            user = User.objects.get(email=email)
            if user:
                prof = Profile.objects.get(user=user)
                if prof.otp == otp:
                    user.set_password(password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.warning(request, "User Password Changed Successfully.")
                    return redirect('login')
                else:
                    messages.warning(request, "Otp not matched Try again.")
            else:
                messages.warning(request, "No user found.")
                return redirect('forget_pass')

    return render(request, 'accounts/verify_otp.html')


def send_mail_registration(email, otp):
    subject = "Account Verification OTP"
    message = f'Your verify otp is :  {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
