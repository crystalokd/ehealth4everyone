from django.urls import path
from .views import doctorclick_view
from .views import HomePageView
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),


    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),

    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),

    path('doctorlogin', LoginView.as_view(template_name='hospital_app/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital_app/patientlogin.html')),
    
    
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),

    path('search/', SearchResultsListView.as_view(), name='search_results'),

    path('profile/', views.ehealth_profile, name='ehealth_profile'),
    path('tables/', views.ehealth_tables, name='ehealth_tables'),

     path('register/', views.Ehealth_register.as_view(template_name='ehealthApp/register.html'), name='ehealth_register'),
]




#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),


    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]




#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),

]