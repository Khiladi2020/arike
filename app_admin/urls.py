from django.urls import path

from . import views

app_name="app_admin"
urlpatterns = [
    path('', views.home_page, name="index"),
    path('facility/',views.FacilityListView.as_view(), name="facility_list"),
    path('facility/<int:pk>',views.FacilityDetailView.as_view(), name="facility_detail"),
    path('facility/create/',views.FacilityCreateView.as_view(), name="facility_form"),
    path('facility/update/<int:pk>',views.FacilityUpdateView.as_view(), name="facility_update"),
    path('facility/delete/<int:pk>',views.FacilityDeleteView.as_view(), name="facility_delete"),
    path('user/',views.UserListView.as_view(), name="user_list"),
    path('user/<int:pk>',views.UserDetailView.as_view(), name="user_detail"),
    path('user/create/',views.UserCreateView.as_view(), name="user_form"),
    path('user/update/<int:pk>',views.UserUpdateView.as_view(), name="user_update"),
    path('user/delete/<int:pk>',views.UserDeleteView.as_view(), name="user_delete"),
]
