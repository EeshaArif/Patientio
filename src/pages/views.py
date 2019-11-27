from django.http import HttpResponse
from django.shortcuts import render

def home_view(request,*args, **kwargs):
	#return HttpResponse("<h1>hello world</h1>")
	return render(request,"index.html",{})

def schedule_check_view(request,*args, **kwargs):
	return render(request,"schedule_check.html",{})

def doctor_view(request,*args, **kwargs):
	print(request.user)
	return HttpResponse("<h1>Find Doctor</h1>")

# Create your views here.
