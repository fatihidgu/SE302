from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from YeOradaApp.forms import RegisteredUserChangeForm, CommentAnswerForm, CommentForm
from YeOradaApp.models import Customer, RegisteredUser, Comment, CommentAnswer, CommentLike, Client


def clientsettings(request):
    error_message1 = ""
    if 'saveChanges' in request.POST:
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        workinghours = request.POST.get('workinghours')
        workingdays = request.POST.get('workingdays')
        info = request.POST.get('info')
        userObject = RegisteredUser.objects.filter(email=request.user.email).first()
        clientObject = Client.objects.filter(userEmail=request.user).first()
        emailCheck = RegisteredUser.objects.filter(email=email)
        usernameCheck = RegisteredUser.objects.filter(username=username)
        if usernameCheck.first() and username != request.user.username:
            error_message1 = "*Username are already used"
            user = request.user
            client = Customer.objects.filter(userEmail=user.email).first()
        else:
            userObject.name = name;
            userObject.surname = surname;
            userObject.username = username;

            clientObject.phone = phone
            clientObject.city = city
            clientObject.address1 = address1
            clientObject.address2 = address2
            clientObject.state = state
            clientObject.workingHours = workinghours
            clientObject.workingDays = workingdays
            clientObject.info = info

            userObject.save()
            clientObject.save()
            return redirect('clientsettings')

    elif 'changePassword' in request.POST:
        passwordChangeForm = PasswordChangeForm(request.user, request.POST)
        if passwordChangeForm.is_valid():
            passwordChangeForm.save()

    elif 'yourEmail' in request.POST:
        if request.POST.get('Email') == request.user.email:
            ruser = RegisteredUser.objects.filter(email=request.user.email)
            ruser.update(is_active=False)
            return redirect('home')
        else:
            print("Error verilecek bitmedi")

    user = request.user
    passwordChangeForm = PasswordChangeForm(request.user)
    client = Client.objects.filter(userEmail=user.email).first()

    return render(request, 'yeoradamain/setting_client.html',
                  {'user': user, 'client': client, 'error_message1': error_message1,
                   'passwordChangeForm': passwordChangeForm, })