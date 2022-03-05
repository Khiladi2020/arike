"""arike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from app_admin.views import home_page, AuthLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('arike/admin-panel/', admin.site.urls),
    path('admin/', include('app_admin.urls')),
    path('patient/', include('patient.urls')),
    path('', home_page, name="home_page"),
    path('login/', AuthLoginView.as_view(), name="auth_login"),
    path('logout/', LogoutView.as_view(), name="auth_logout"),
]
