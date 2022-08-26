from django.contrib import admin
from .models import reports, patient, employee, lab_equipment

# Register your models here.

admin.site.register(reports)
admin.site.register(patient)
admin.site.register(employee)
admin.site.register(lab_equipment)
