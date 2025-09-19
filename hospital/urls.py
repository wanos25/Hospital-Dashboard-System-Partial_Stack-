from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# صفحة رئيسية
def home(request):
    return render(request, "Futuristic-Hospital-Dashboard.html")

urlpatterns = [
    path("", home, name="home"),  
    path("admin/", admin.site.urls),
    path("api/doctors/", include("doctors.urls")),
    path("api/patients/", include("patients.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/pharmacy/", include("pharmacy.urls")),
    path("api/users/", include("users.urls")),
]
