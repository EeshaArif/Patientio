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

def about(request):
    context = {
    'about': About.objects.get(pk = 1)
    }
    return render(request, "about.html", context)

def appointments(request):
    context = {
    'appointments': Appointment.objects.all()
    }
    return render(request, "appointments_list.html", context)

def doctor_list(request):
    context = {
    'doctors': Doctor.objects.all()
    }
    return render(request, "doctor_list_booking.html", context)

def lab_reports(request):
    context = {
    'reports': Report.objects.all()
    }
    return render(request, "lab_reports_list.html", context)

def patient_info(request):
    context = {
    'patient': Patient.objects.all()
    }
    return render(request, "patient_info.html", context)

def services(request):
    context = {
    'service': Service.objects.all()
    }
    return render(request, "services.html", context)

def single_doctor(request,doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, "single_doctor_booking.html", {'doctor': doctor})

def single_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, "single_report.html", {'report': report})


def single_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'single_service.html', {'service': service, 'services_info' : Service.objects.all()})

def booking(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.POST.get('Appointment Date') and request.POST.get('Appointment Time'):
        appointment = doctor.appointmemt.get(pk=request.POST.get('disease'))
        doctor.appointment.date=request.POST.get('Appointment Date')
        doctor.appointment.time=request.POST.get('Appointment Time')
        return HttpResponseRedirect('appointments_list.html')
    else:
        appointment.save()
        return HttpResponseRedirect('appointments_list.html')

def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments_list')
    return redirect('appointments_list')

def lab_report_delete(request, report_id):
    lab_report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':
        lab_report.delete()
        return redirect('lab_reports')
    return redirect('lab_reports')