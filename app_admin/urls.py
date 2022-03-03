from django.urls import path

from . import views

app_name="app_admin"
urlpatterns = [
    path('', views.index, name="index")
]
