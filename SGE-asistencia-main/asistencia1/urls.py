from django.contrib import admin
from django.urls import path
from asistencia import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Inicio
    path('', views.inicio, name='inicio'),

    # Toma de asistencia
    path('asistencia/', views.tomar_asistencia, name='tomar_asistencia'),

    # Consulta de registros
    path('asistencia/lista/', views.lista_asistencia, name='lista_asistencia'),

    # Reportes
    path('asistencia/reporte/', views.reporte_asistencia, name='reporte_asistencia'),
]
