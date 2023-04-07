from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
from .models import UserModel
from django.contrib.auth.decorators import login_required
import re


def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        department = request.POST.get('department', '')

        if password != password2:
            return render(request, 'accounts/signup.html', {'error': "패스워드를 확인해주세요!"})
        else:
            if username == '' or password == '':
                return render(request, 'accounts/signup.html', {'error': "이름, 비밀번호는 필수입니다!"})

            exist_user = get_user_model().objects.filter(username=username)
            exist_email = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'accounts/signup.html', {'error': "이미 있는 이름입니다."})
            elif exist_email:
                return render(request, 'accounts/signup.html', {'error': "이미 있는 이메일입니다."})
            else:
                UserModel.objects.create_user(username=username, password=password, email=email, department=department)
                return redirect('/sign-in')


def signin(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/signin.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'accounts/signin.html', {'error': "이름과 패스워드를 확인해주세요."})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

