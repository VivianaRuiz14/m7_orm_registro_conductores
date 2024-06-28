from typing import Any
from main.models import Estudiante, Curso, Direccion, Profesor
from main.services import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        c = crear_curso('C01', 'lectura rapida', 1)
        e = crear_estudiante('33.333.333-3', )
    