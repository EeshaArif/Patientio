from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.profile,name='profile'),
    path('about_us/',views.about, name='about_us'),
    path('appointments/', views.appointments, name = 'appointments_list'),
    path('doctor_list/', views.doctor_list, name = 'doctor_list'),
    path('lab_reports/', views.lab_reports, name = 'lab_reports'),
    path('services/', views.services, name = 'services'),
    path('<int:doctor_id>/doctor/',views.single_doctor, name='doctor_info'),
    path('<int:report_id>/report/',views.single_report, name='report_detail'),
    path('<int:service_id>/service/',views.single_service, name='service_detail'),
    path('delete_appointment/<int:appointment_id>', views.appointment_delete, name='appointment_delete'),
    path('delete_report/<int:report_id>', views.lab_report_delete, name='lab_report_delete'),
    path('booking/<int:doctor_id>', views.booking, name ='booking'),
    path('contactus', views.contactus, name = 'contactus'),
    path('patient_info', views.patient_info, name = 'patient_info'),
]
