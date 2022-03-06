from django.urls import path

from . import views

app_name = "patient"
urlpatterns = [
    path('', views.PatientListView.as_view(), name="patient_list"),
    path('<int:pk>/', views.PatientDetailView.as_view(), name="patient_detail"),
    path('create/', views.PatientCreateView.as_view(), name="patient_form"),
    path('update/<int:pk>', views.PatientUpdateView.as_view(), name="patient_update"),
    path('<int:patient_id>/family/',views.FamilyDetailListView.as_view(), name="familydetail_list"),
    path('<int:patient_id>/family/create/',views.FamilyDetailCreateView.as_view(), name="familydetail_form"),
    path('<int:patient_id>/family/update/<int:pk>',views.FamilyDetailUpdateView.as_view(), name="familydetail_update"),
    path('<int:patient_id>/disease/',views.PatientDiseaseListView.as_view(), name="patientdisease_list"),
    path('<int:patient_id>/disease/create/',views.PatientDiseaseCreateView.as_view(), name="patientdisease_form"),
    path('<int:patient_id>/disease/update/<int:pk>',views.PatientDiseaseUpdateView.as_view(), name="patientdisease_update"),
    path('<int:patient_id>/visit/',views.PatientVisitListView.as_view(), name="patientvisit_list"),
    path('<int:patient_id>/visit/<int:pk>',views.PatientVisitDetailView.as_view(), name="patientvisit_detail"),
    path('schedule/',views.VisitScheduleListView.as_view(), name="schedule_list"),
    path('schedule/create/',views.VisitScheduleCreateView.as_view(), name="schedule_form"),
    path('schedule/<int:pk>/detail/',views.VisitScheduleDetailView.as_view(), name="schedule_detail"),
    path('schedule/<int:schedule_id>/visit/', views.VisitCreateView.as_view(), name="visit_form"),
]
