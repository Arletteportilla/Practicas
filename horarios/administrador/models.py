from django.db import models
# Create your models here.

class Persona(models.Model):
    choices_genero = [('h','Hombre'),('M','Mujer')]
    
    nombres = models.CharField(verbose_name = "nombres", max_length=50)
    apellidos = models.CharField(verbose_name ="apellidos", max_length=50)
    genero = models.CharField(verbose_name ="genero", max_length=50, choices = choices_genero)
    telefono = models.CharField(verbose_name ="telefono", max_length=50)
    email = models.CharField(verbose_name ="email", max_length=50)


class Estudiante(Persona):
    numeroCarnet = models.IntegerField(verbose_name = "numeroCarnet")

class Docente(Persona):
    choices_funciones = [('Docencia','Docente'),('Investigacion','Investigacion'),('Vinculacion','Vinculacion'),('Gestion','Gestion')]

    codigoDocente = models.CharField(verbose_name ="codigoDocente", max_length=50)
    especialidad = models.CharField(verbose_name ="especialidad", max_length=50)
    funciones = models.CharField(verbose_name ="funciones", max_length=50, choices = choices_funciones)

class Coordinador(Persona):
    codigoCoordinador = models.CharField(verbose_name ="codigoCoordinador", max_length=50)

class Facultad(models.Model):
    nombreFacultad = models.CharField(verbose_name = "nombreFacultad", max_length=100)
    descripcion = models.CharField(verbose_name ="descripcion", max_length=50)
    fechaCreacion = models.DateField(verbose_name ="fechaCreacion", auto_now=True, auto_now_add=True)

class Carrera(models.Model): 
    nombreCarrera = models.CharField(verbose_name ="nombreCarrera", max_length=50)
    duracionCarrera = models.IntegerField(verbose_name ="duracionCarrera")
    codigoCarrera =  models.CharField(verbose_name ="codigoCarrera", max_length=50)
    tipoAsignatura = models.CharField(verbose_name ="tipoAsignatura", max_length=50)

class Malla(models.Model):
    choices_anioMalla = [('2019','2019'),('2020','2020'),('2021','2021'),('2022','2023')]
    nombreMalla = models.CharField(verbose_name ="nombreMalla", max_length=50)
    anioMalla = models.CharField(verbose_name ="anioMalla", max_length=50,choices= choices_anioMalla)

class Ciclo(models.Model):
    numeroCiclo = models.IntegerField(verbose_name"numeroCiclo")
    nombreCiclo = models.CharField(verbose_name = "nombreCiclo", max_length=50)
    fechaInicio = models.DateField(verbose_name = "fechaInicio")
    fechaFin = models.DateField(verbose_name = "fechaFin")

class  Ofertador(models.Model):
    fechaOfertada = models.DateField(verbose_name = "fechaOfertada")

class materia(models.Model):
    duracionClase = models.IntegerField(verbose_name ="duracionClase")
    numeroEstudiante = models.IntegerField(verbose_name ="numeroEstudiante")
    horasClase = models.IntegerField(verbose_name = "numeroEstudiantes")
    nombreMateria = models.CharField(verbose_name = "nombreMateria", max_length=50)
    materiaAprobada = models.BooleanField(verbose_name = "materiaAprobada")

class Aulas(models.Model):
    nombreAula = models.CharField(verbose_name ="nombreAula", max_length=50)
    capacidadAula = models.IntegerField(verbose_name ="capacidadAula")
    numeroAula = models.IntegerField(verbose_name ="numeroAula")
    horaInicio = models.TimeField(verbose_name ="horaInicio")
    horaFin = models.TimeField(verbose_name ="horaFin")

class Paralelo(models.Model): 
    numeroParalelo = models.IntegerField(verbose_name ="numeroParalelo")
    numeroEstudiantes =models.IntegerField(verbose_name ="numeroEstudiantes")
    nombreParalelo = models.CharField(verbose_name ="nombreParalelo", max_length=50)
 



    