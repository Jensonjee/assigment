from django.contrib import admin
from .models import student,facultyreg,events,report

# Register your models here.
admin.site.register(student)
admin.site.register(facultyreg)
admin.site.register(events)
admin.site.register(report)