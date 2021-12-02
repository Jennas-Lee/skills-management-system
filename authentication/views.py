from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

import re


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        response_data = {
            'error': "",
            'email': email,
            'password': password
        }

        if not (email and password):
            response_data['error'] = "이메일과 비밀번호를 입력하세요."
        else:
            user = User.objects.filter(email=email)

            if user.count() <= 0:
                response_data['error'] = "이메일을 찾을 수 없습니다."
            elif user.first().is_active is False:
                response_data['error'] = "승인이 완료되지 않았거나 거부되었습니다."
            elif check_password(password, user.first().password) is False:
                response_data['error'] = "비밀번호가 잘못되었습니다."
            else:
                login(request, authenticate(request, username=email, password=password))

                return HttpResponseRedirect(reverse('index'))

        return render(request, 'signin.html', response_data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password_confirm = request.POST.get('password_confirm', None)
        name = request.POST.get('name', None)

        response_data = {
            'error': "",
            'email': email,
            'password': password,
            'password_confirm': password_confirm,
            'name': name
        }

        if not (email and password and password_confirm and name):
            response_data['error'] = "모든 항목을 입력하세요."
        elif re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$@$!%*#?&]{8,}$', password) is None:
            response_data['error'] = "비밀번호는 8~20자로, 문자와 숫자를 포함해야합니다."
        elif password != password_confirm:
            response_data['error'] = "비밀번호가 일치하지 않습니다."
        elif User.objects.filter(email=email).count() > 0:
            response_data['error'] = "이미 존재하는 이메일입니다."
        else:
            user = User.objects.create_user(name, email, password)
            user.is_active = False
            user.save()

            return HttpResponse('<script>alert("회원가입이 완료되었습니다. 승인 후 사용가능합니다."); location.href="/";</script>')

        return render(request, 'signup.html', response_data)


def signout(request):
    if request.user.is_authenticated:
        logout(request)

    return HttpResponseRedirect(reverse('index'))


def mypage(request):
    if request.method == 'GET':
        response_data = {
            'email': "",
            'name': ""
        }

        if request.user.is_authenticated:
            response_data['email'] = request.user.email
            response_data['name'] = request.user.username

        return render(request, 'mypage.html', response_data)

    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        change_password = request.POST.get('change_password', None)
        change_password_confirm = request.POST.get('change_password_confirm', None)
        name = request.POST.get('name', None)

        response_data = {
            'error': "",
            'success': "",
            'email': email,
            'password': password,
            'change_password': change_password,
            'change_password_confirm': change_password_confirm,
            'name': name
        }

        if not (email and name):
            response_data['error'] = "이메일과 이름은 반드시 입력해야합니다."
        elif not password:
            response_data['error'] = "비밀번호를 입력하세요."
        elif request.user.check_password(password) is False:
            response_data['error'] = "비밀번호가 잘못되었습니다."
        elif email != request.user.email and User.objects.filter(email=email).count() > 0:
            response_data['error'] = "이메일을 변경할 수 없습니다. 이미 존재하는 이메일입니다."
        elif change_password is not None and change_password != "" and \
                re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$@$!%*#?&]{8,}$', change_password) is None:
            response_data['error'] = "변경할 비밀번호는 8~20자로, 문자와 숫자를 포함해야합니다."
        elif change_password is not None and change_password != change_password_confirm:
            response_data['error'] = "변경할 비밀번호가 일치하지 않습니다."
        else:
            user = request.user

            user.set_password(change_password)
            user.email = email
            user.name = name
            user.save()
            update_session_auth_hash(request, user)

            response_data['success'] = "정보가 변경되었습니다."

        return render(request, 'mypage.html', response_data)
