from list_for_shop.models import ListShop
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def home(request):
    list_shop = ListShop.objects.all()[:3]
    return render(request, 'home/home.html', {'list_shop': list_shop})


def register(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        context = {'error': []}
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if username and password1 and password2 and email and first_name and last_name:
            if password1 == password2:
                users = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                if users is not None:
                    login(request, users)
                    return redirect('home:home')

            else:
                context['error'].append("your password isn't Set")
                return render(request, 'home/register.html', context)

        else:
            context['error'].append('Confirm your form')
            return render(request, 'home/register.html', context)

    return render(request, 'home/register.html', {})


def login_user(request):
    context = {'error': []}

    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(User, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                context['error'].append('username or password is not correct')
                return render(request, 'home/login.html', context)
        else:
            context['error'].append('please confirm username and password')
            return render(request, 'home/login.html', context)

    return render(request, 'home/login.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'home/home.html', {})

