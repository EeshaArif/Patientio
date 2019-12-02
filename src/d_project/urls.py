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
#from pages.views import home_view, contact_view, about_view, social_view

urlpatterns = [
    path('', home_view, name='home'),
    path('findDoctor/',doctor_view, name='findDoctor'),
    path('appointments/',appointment_view, name='appointments'),
    path('departments/',departments_view, name='departments'),
    path('contactus/',contactus_view, name='contactus'),
    path('aboutus/',aboutus_view, name='aboutus'),
    path('schedule/',schedule_check_view),
  #  path('contact/',contact_view),
   # path('about/',about_view),
    #path('social/',social_view),
    path('admin/', admin.site.urls),
]
