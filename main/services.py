from main.models import *
from datetime import date

def crear_curso(codigo, nombre, version, profesor):
    curso = Curso(codigo=codigo, nombre=nombre, version=version, profesor=profesor)
    curso.save()
    
def crear_estudiante(rut, nombre,apellido, fecha_nac):
    estudiante =Estudiante(rut=rut, nombre=nombre,apellido=apellido, fecha_nac=fecha_nac, activo=True, created=date.today(), update=date.today())
    estudiante.save()
    
def crear_profesor(rut, nombre, apellido):
    profesor= profesor(rut=rut, nombre=nombre, apellido=apellido, created=date.now(), update=date.now())
    profesor.save()
    
    
    
    
