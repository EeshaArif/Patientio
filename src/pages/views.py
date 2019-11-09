from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request,"index.html",{})
	#{} context

def contact_view(request,*args,**kwargs):
	return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
	return render(request,"aboutus.html",{})

def social_view(request,*args,**kwargs):
	return render(request,"social.html",{})
