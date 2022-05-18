from django.contrib import admin

from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')

@admin.register(Measurement)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'temperature', 'created_at')