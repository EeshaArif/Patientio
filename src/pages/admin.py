from django.contrib import admin
from .models import About,Appointment,Doctor,LabDoc,Nurse,Patient,Receptionist,Report,Service,Person,History,Curriculum,Specialization,Payment
# Register your models here.

admin.site.register(About)
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(LabDoc)
admin.site.register(Nurse)
admin.site.register(Receptionist)
admin.site.register(Report)
admin.site.register(Service)
admin.site.register(Person)
admin.site.register(History)
admin.site.register(Curriculum)
admin.site.register(Payment)
admin.site.register(Specialization)
