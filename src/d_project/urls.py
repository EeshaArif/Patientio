"""d_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from pages.views import home_view,doctor_view,schedule_check_view,appointment_view,departments_view,contactus_view,aboutus_view
from pages import views
#from pages.views import home_view, contact_view, about_view, social_view

urlpatterns = [
    path('', home_view, name='home'),
    path('findDoctor/',doctor_view, name='findDoctor'),

    path('departments/',departments_view, name='departments'),
    path('contactus/',contactus_view, name='contactus'),
    path('aboutus/',aboutus_view, name='aboutus'),
    #
    path('about_us/',views.about, name='about_us'),
    path('appointments/', views.appointments, name = 'appointments_list'),
    path('doctor_list/', views.doctor_list, name = 'doctor_list'),
    path('lab_reports/', views.lab_reports, name = 'lab_reports'),
    path('patient_info/', views.patient_info, name = 'patient_info'),
    path('services/', views.services, name = 'services'),
    path('<int:doctor_id>/doctor/',views.single_doctor, name='doctor_info'),
    path('<int:report_id>/report/',views.single_report, name='report_detail'),
    path('<int:service_id>/service/',views.single_service, name='service_detail'),
    path('<int:doctor_id>/booking/',views.booking, name='appointment'),
    path('delete_appointment/<int:appointment_id>', views.appointment_delete, name='appointment_delete'),
    path('delete_report/<int:report_id>', views.lab_report_delete, name='lab_report_delete'),
    path('booking/<int:doctor_id>',views.booking, name='booking'),
  #  path('contact/',contact_view),
   # path('about/',about_view),
    #path('social/',social_view),
    path('schedule/',schedule_check_view),
    path('admin/', admin.site.urls),
]
