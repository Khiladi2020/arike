from django.urls import path

from . import views

app_name="app_admin"
urlpatterns = [
    path('', views.index, name="index"),
    path('facility/',views.FacilityListView.as_view(), name="facility_list"),
    path('facility/<int:pk>',views.FacilityDetailView.as_view(), name="facility_detail"),
    path('facility/create/',views.FacilityCreateView.as_view(), name="facility_form"),
    path('facility/update/<int:pk>',views.FacilityUpdateView.as_view(), name="facility_update"),
    path('facility/delete/<int:pk>',views.FacilityDeleteView.as_view(), name="facility_delete"),
]
