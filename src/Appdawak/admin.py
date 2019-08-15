from django.contrib import admin

from .models import Medicine

class MedicineAdmin(admin.ModelAdmin):
    list_display = ("title", "price",)

admin.site.register(Medicine, MedicineAdmin)