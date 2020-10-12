from django.contrib import admin
from .models import Department, Technics, SendRecord,Type

# Register your models here.
admin.site.register(Department)
admin.site.register(Technics)
admin.site.register(SendRecord)
admin.site.register(Type)