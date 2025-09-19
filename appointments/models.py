from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled")],
        default="scheduled"
    )

    def __str__(self):
        return f"Appointment: {self.patient.name} with {self.doctor.name} on {self.date}"
