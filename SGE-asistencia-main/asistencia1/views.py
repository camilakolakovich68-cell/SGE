from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Sistema de Control de Asistencia")

def tomar_asistencia(request):
    return HttpResponse("Registrar asistencia")

def lista_asistencia(request):
    return HttpResponse("Lista de asistencias registradas")

def reporte_asistencia(request):
    return HttpResponse("Reporte de asistencia")