from django.shortcuts import render, get_object_or_404
from .models import About,Appointment,Doctor,Report,Service,History
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
     return render(request, "index.html", {})
def about(request):
    context = {
    'about': About.objects.all()
    }
    return render(request, "about.html", context)

def doctor_list(request):
    context = {
    'doctors': Doctor.objects.all()
    }
    return render(request, "doctor_list_booking.html", context)

def services(request):
    context = {
    'service': Service.objects.all()
    }
    return render(request, "services.html", context)

@login_required
def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments_list')
    return redirect('appointments_list')

@login_required
def lab_report_delete(request, report_id):
    lab_report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':
        lab_report.delete()
        return redirect('lab_reports')
    return redirect('lab_reports')

@login_required
def lab_reports(request):
    reports = Report.objects.filter(user = request.user)
    if reports:
        return render(request, "lab_reports_list.html", {'reports': reports})
    else:
        message = "No records Found"
        return render(request, "lab_reports_list.html", {'message': message})

@login_required
def appointments(request):
    appointments = Appointment.objects.filter(user = request.user)
    if appointments:
        return render(request, "appointments_list.html", {'appointments': appointments})
    else:
        message = "No records Found"
        return render(request, "appointments_list.html", {'message': message})

def single_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, "single_report.html", {'report': report})

def single_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'single_service.html', {'service': service, 'services_info' : Service.objects.all()})

def single_doctor(request,doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, "single_doctor_booking.html", {'doctor': doctor})

@login_required
def profile(request):
    history = History.objects.filter(user = request.user)
    if history:
        return render(request, "profile.html", {'history': history})
    else:
        message = "No records Found"
        return render(request, "profile.html", {'message': message})

@login_required
def booking(request, doctor_id):
    if request.method == 'POST' and request.POST.get('Appointment Date') and request.POST.get('Appointment Time'):
        disease = request.POST.get('issue')
        date=request.POST.get('Appointment Date')
        time=request.POST.get('Appointment Time')
        doctor = doctor_id
        user = request.user
        appointment = Appointment.objects.create(date=date, time=time, user=user, disease_option=disease, doctor = doctor)
        appointment.save()
        appointments = Appointment.objects.filter(user = request.user)
        return render(request, 'appointments_list.html', {'appointments': appointments})
    else:
        appointments = Appointment.objects.filter(user = request.user)
        return render(request, 'appointments_list.html', {'appointments': appointments})

def contactus(request):
    pass

def patient_info(request):
    pass
