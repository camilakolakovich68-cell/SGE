from django.contrib import admin
from .models import RegistroAsistencia


@admin.register(RegistroAsistencia)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'materia', 'fecha', 'estado')
    list_filter = ('fecha', 'estado', 'materia')
    search_fields = ('alumno__nombre',)