from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.OneToOneField(Estudiante, related_name='direccion', on_delete=models.CASCADE)
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.ForeignKey(Profesor, related_name='cursos', on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')
    
    