from django.test import TestCase
from .models import Asistencia
from datetime import date, time


class AsistenciaModelTest(TestCase):

    def test_creacion_asistencia(self):
        asistencia = Asistencia.objects.create(
            nombre="Juan Pérez",
            fecha=date.today(),
            hora=time(8, 0),
            presente=True
        )

        self.assertEqual(asistencia.nombre, "Juan Pérez")
        self.assertTrue(asistencia.presente)
        