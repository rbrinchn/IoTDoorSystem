"""IoTDoorSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DoorSystem import views as system

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', system.index_render, name="index"),
    path('dashboard/', system.dashboard_render, name="dashboard"),
    path('login/', system.login_render, name="login"),
    path('logout/', system.logout_user, name="logout"),
    path('users/', system.users_render, name='user_overview'),
    path('users/add/', system.create_new_user, name="new_user"),
    path('user/edit/<str:user_id>/', system.create_new_user, name="edit_user"),
    path('virtual_keys/', system.virtual_key_render, name='keys_overview'),
    path('virtual_keys/add/', system.virtual_key_modal, name="new_key"),
    path('virtual_keys/edit/<str:key_id>', system.virtual_key_modal, name="edit_key"),
    path('test/', system.test_render, name="test_url"),


]
