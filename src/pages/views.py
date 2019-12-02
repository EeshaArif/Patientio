from django.http import HttpResponse
from django.shortcuts import render

def home_view(request,*args, **kwargs):
	#return HttpResponse("<h1>hello world</h1>")
	return render(request,"index.html",{})

def schedule_check_view(request,*args, **kwargs):
	return render(request,"schedule_check.html",{})

def doctor_view(request,*args, **kwargs):
	print(request.user)
	return render(request,"doctor.html",{})
	#return HttpResponse("<h1>Find Doctor</h1>")
def appointment_view(request,*args, **kwargs):
	print(request.user)
	return render(request,"appointments.html",{})

def departments_view(request,*args, **kwargs):
	print(request.user)
	return render(request,"departments.html",{})

def contactus_view(request,*args, **kwargs):
	print(request.user)
	return render(request,"contactus.html",{})

def aboutus_view(request,*args, **kwargs):
	print(request.user)
	return render(request,"aboutus.html",{})
# Create your views here.

