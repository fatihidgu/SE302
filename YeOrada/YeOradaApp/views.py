from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
from YeOradaApp.forms import RegisteredUserCreationForm, CommentForm
from YeOradaApp.models import Comment, Customer, Client

from .views_ahmet import *
from .views_ali import *
from .views_fatih import *
from .views_yaren import *


def index(request):
    clients = Client.objects.all().order_by('-rateCount')[:10]

    return render(request, 'yeoradamain/index.html', {'clients':clients,})


def signin(request):
    control = False
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        registeredUser = RegisteredUser.objects.filter(email=form.data.get('username')).first()

        if (registeredUser is not None) and (not registeredUser.is_active):
            registeredUser.is_active = True
            control = True
            registeredUser.save()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'yeoradamain/index.html', {'control': control})
        else:
            error_message = "* Wrong Email or Password."
    else:
        error_message = ""
        form = AuthenticationForm()
    return render(request, 'yeoradamain/signin.html', {'form': form, 'error_message': error_message, })


def signup(request):
    error_message1 = ""
    error_message2 = ""
    if request.method == "POST":
        form = RegisteredUserCreationForm(request.POST)
        if form.is_valid():
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            if pass1 == pass2:
                cb = request.POST.get('cb')
                if not cb:
                    error_message1 = "* You must accept the Terms of Service and the Content Policy."
                else:
                    form.save()
                    user = RegisteredUser.objects.filter(email=form.cleaned_data['email']).first()
                    customer = Customer(userEmail=user)
                    customer.save()
                    return redirect('signin')
            else:
                error_message2 = "* Passwords doesn't match."
    else:
        form = RegisteredUserCreationForm()
    return render(request, 'yeoradamain/signup.html', {'form': form, 'error_message1': error_message1, 'error_message2': error_message2, })