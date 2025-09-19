from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "patient", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("doctor__name", "patient__name")
