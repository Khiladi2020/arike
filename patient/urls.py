from django.urls import path

from . import views

app_name = "patient"
urlpatterns = [
    path('', views.PatientListView.as_view(), name="patient_list"),
    path('<int:pk>/', views.PatientDetailView.as_view(), name="patient_detail"),
    path('create/', views.PatientCreateView.as_view(), name="patient_form"),
    path('update/<int:pk>', views.PatientUpdateView.as_view(), name="patient_update"),
]
