from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "expiry_date")
    search_fields = ("name",)
    list_filter = ("expiry_date",)
