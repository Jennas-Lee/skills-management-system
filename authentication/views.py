from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def signin(request):
    if request.method == 'GET':
        return render(request, 'auth/signin.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate()
