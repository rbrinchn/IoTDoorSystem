from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from datetime import datetime


# from JobTeamLogs.models import Log
# from JobTeamLogs.views import CreateLog


# Create your views here.
def test_render(request):
    return render(request, 'DoorSystem/test.html')


def index_render(request):
    authenticated = request.user.is_authenticated
    is_active = request.user.is_active

    if authenticated and is_active:
        return redirect('dashboard')
        # If user is authenticated but not active
    elif authenticated and not is_active:
        return redirect('login', is_active=False)
    else:
        return redirect('login')


def login_render(request):
    if request.method == "GET":
        return render(request, 'DoorSystem/Authentication/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(str("USER: ") + str(user))
        # User is only none if the username or password was incorrect
        if user is None:
            request.method = "GET"
            # checks if username exist and if it's due to disabled user
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)

                if not user.is_active:
                    error_message = "Din bruger er ikke aktiv længere"
                    return render(request, 'DoorSystem/Authentication/login.html', {'error_message': error_message})

            # If the statement above is not correct, credentials was wrongly entered
            error_message = "Forkert brugernavn eller adgangskode"
            return render(request, 'DoorSystem/Authentication/login.html', {'error_message': error_message})
        else:
            login(request, user)

            # Checks for virtual key
            if user.is_active and (user.is_staff or user.is_superuser):
                print("HIIII")
                return redirect('index')
            elif user.is_active:  # User is active - meaning it's a virtual key
                key = VirtualKey.objects.get(user=user)
                now = datetime.now()

                # Checks if key is still active
                if key.active_from < now < key.active_to:
                    return render(request, 'DoorSystem/find-new-name.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def dashboard_render(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'DoorSystem/index.html')
    else:
        return redirect('login')


def users_render(request):
    users = User.objects.filter(is_staff=True).order_by('-is_active')
    return render(request, 'DoorSystem/table.html', {'users': users})


def create_new_user(request, user_id=0):
    if request.method == "GET":
        if user_id == 0:
            return render(request, "DoorSystem/Modal-Content/user-modal.html")
        else:
            user = User.objects.get(id=user_id)
            return render(request, "DoorSystem/Modal-Content/user-modal.html", {'user_form': user})
    elif request.method == "POST":
        if user_id == 0:
            username = request.POST['input-username']
            password = request.POST['input-password']
            user = User.objects.create_user(username=username, password=password)
            user.first_name = request.POST['input-firstname']
            user.last_name = request.POST['input-lastname']
            user.is_active = True
            user.is_staff = True
            user.save()
        else:
            user = User.objects.get(id=user_id)
            user.username = request.POST['input-username']
            user.first_name = request.POST['input-firstname']
            user.last_name = request.POST['input-lastname']
            user.save()
        return redirect('user_overview')


def virtual_key_render(request):
    virtual_keys = VirtualKey.objects.all()
    return render(request, 'DoorSystem/find-new-name.html', {'keys': virtual_keys})


def virtual_key_modal(request, key_id=0):
    if request.method == "GET":
        if key_id != 0:
            key = VirtualKey.objects.get(id=key_id)
            return render(request, 'DoorSystem/Modal-Content/virtual-key-modal.html', {'virtual_key': key})
        else:
            return render(request, 'DoorSystem/Modal-Content/virtual-key-modal.html')
    elif request.method == "POST":
        if key_id != 0:
            key = VirtualKey.objects.get(id=key_id)
            key.active_from = request.POST['input-active-from']
            key.active_to = request.POST['input-active-to']
            key.save()
        else:
            # New Key
            username = request.POST['input-username']
            password = request.POST['input-password']
            user = User.objects.create(username=username, password=password)
            user.is_active = True
            user.save()

            key = VirtualKey()
            key.user = user
            key.created_by = request.user
            key.active_from = request.POST['input-active-from']
            key.active_to = request.POST['input-active-to']
            key.save()
            user.save()
        return redirect('keys_overview')
