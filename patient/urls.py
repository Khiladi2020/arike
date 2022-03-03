from django.urls import path

from . import views

urlpatterns = [
    path('', views.PatientListView.as_view(), name="patient_list"),
    path('<int:pk>/', views.PatientDetailView.as_view(), name="patient_detail"),
    path('create/', views.PatientCreateView.as_view(), name="patient_form"),
]
