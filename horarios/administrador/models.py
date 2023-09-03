from django.db import models
# Create your models here.

class Persona(models.Model):
    choices_genero = [('h','Hombre'),('M','Mujer')]
    
    nombres = models.CharField(verbose_name = "nombres", max_length=50)
    apellidos = models.CharField(verbose_name ="apellidos", max_length=50)
    genero = models.CharField(verbose_name ="genero", max_length=50, choices = choices_genero)
    telefono = models.CharField(verbose_name ="telefono", max_length=50)
    email = models.CharField(verbose_name ="email", max_length=50)
    
    def __str__(self):
        return self.nombres 

class Ciclo(models.Model):
    numeroCiclo = models.IntegerField(verbose_name ="numeroCiclo")
    nombreCiclo = models.CharField(verbose_name = "nombreCiclo", max_length=50)
    
    def __str__(self):
        return self.nombreCiclo
    
class Materia(models.Model):
    duracionClase = models.IntegerField(verbose_name ="duracionClase")
    nombreMateria = models.CharField(verbose_name = "nombreMateria", max_length=50)
    ciclo = models.ManyToManyField(Ciclo, verbose_name="ciclo",null= True, blank=True)

    def __str__(self):
        return self.nombreMateria 
    
class Paralelo(models.Model): 
    numeroParalelo = models.IntegerField(verbose_name ="numeroParalelo")
    numeroEstudiantes =models.IntegerField(verbose_name ="numeroEstudiantes")
    nombreParalelo = models.CharField(verbose_name ="nombreParalelo", max_length=50)
    materia = models.ManyToManyField(Materia, verbose_name ="materia",null= True, blank=True)
    def __str__(self):
        return self.nombreParalelo

class Aulas(models.Model):
    nombreAula = models.CharField(verbose_name ="nombreAula", max_length=50)
    capacidadAula = models.IntegerField(verbose_name ="capacidadAula")
    numeroAula = models.IntegerField(verbose_name ="numeroAula")
    def __str__(self):
        return self.nombreAula


class Estudiante(Persona):
    choices_nivelIngles = [('1','Nivel1'),('2','Nivel2'),('3','Nivel3'),('4','Nivel4'),('5','Nivel5'),('6','Nivel6'),('C','Completado'),('N','Ninguno')]
    nivelIngles = models.CharField(verbose_name ="nivelIngles", max_length=50, choices = choices_nivelIngles, null= True, blank= True)
    numeroCarnet = models.IntegerField(verbose_name = "numeroCarnet")

        
class Funciones(models.Model):
    nombreFunciones = models.CharField(verbose_name ="nombreFunciones", max_length=50, null=True, blank=True)
    def __str__(self):
        return self.nombreFunciones

class Docente(Persona):
    materia = models.ManyToManyField(Materia,related_name= "docente_materia", null=True, blank=True)#1a muchos
    codigoDocente = models.CharField(verbose_name ="codigoDocente", max_length=50)
    especialidad = models.CharField(verbose_name ="especialidad", max_length=50)
    funciones = models.ManyToManyField(Funciones, verbose_name= "funciones", null= True, blank= True)
    limiteHoras = models.IntegerField(verbose_name= "limiteHoras", max_length=50, null= True, blank= True)

class Coordinador(Persona):
    codigoCoordinador = models.CharField(verbose_name ="codigoCoordinador", max_length=50)


class Facultad(models.Model):
    nombreFacultad = models.CharField(verbose_name = "nombreFacultad", max_length=100)
    descripcion = models.CharField(verbose_name ="descripcion", max_length=50)
    #fechaCreacion = models.DateField(verbose_name ="fechaCreacion", auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.nombreFacultad
    
class Carrera(models.Model): 
    nombreCarrera = models.CharField(verbose_name ="nombreCarrera", max_length=100)
    anioCarrera = models.IntegerField(verbose_name ="aniocarrera", null=True,blank=True)
    numeroTotalCiclos = models.IntegerField(verbose_name="numeroTotalCiclos",null=True,blank=True )
    codigoCarrera =  models.CharField(verbose_name ="codigoCarrera", max_length=50)
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE,null=True,blank=True)#1 a muchos cascade borrar todo en cascada
    coordinador = models.ForeignKey(Coordinador,on_delete=models.RESTRICT, null=True,blank=True )#uno a uno restringe el borrado
    
    def __str__(self):
        return self.nombreCarrera
    
class Malla(models.Model):
    choices_anioMalla = [('2019','2019'),('2020','2020'),('2021','2021'),('2022','2023')]
    choices_campus = [('G','Guayaquil'),('Q','Quito'),('l','Loja')]
    carrera = models.ForeignKey(Carrera, verbose_name= "carrera", on_delete=models.CASCADE, null = True, blank = True)
    campus = models.CharField(verbose_name = "campus", max_length=50, choices= choices_campus, null= True, blank = True)
    nombreMalla = models.CharField(verbose_name ="nombreMalla", max_length=50)
    anioMalla = models.CharField(verbose_name ="anioMalla", max_length=50,choices= choices_anioMalla)
    ciclo = models.ManyToManyField(Ciclo,related_name= "malla_materia", null=True, blank=True) #relacion muchos a muchos 
    
    def __str__(self):
        return self.nombreMalla
   
class PeriodoAcademico(models.Model):
    fechaInicio = models.DateField(verbose_name="fechaInicio")
    fechaFin = models.DateField(verbose_name="fechaFin")
    nombrePeriodoAcademico = models.CharField(verbose_name="nombrePeriodoAcademico", max_length=50)
    ciclo = models.ManyToManyField(Ciclo, verbose_name= "Ciclos",null = True, blank=True)
    malla = models.ManyToManyField( Malla, verbose_name="Mallas",null = True,  blank=True)
    
    def __str__(self):
        return self.nombrePeriodoAcademico
    
class  Ofertador(models.Model):
    nombreOfertador = models.CharField(verbose_name= "nombreOfertador", max_length=50,null=True,blank=True)
    fechaOfertada = models.DateField(verbose_name = "fechaOfertada")
    ciclo = models.ManyToManyField(Ciclo,related_name= "ofertador_ciclo", null=True, blank=True) #relacion muchos a muchos 
    periodoAcademico = models.OneToOneField(PeriodoAcademico, related_name= "ofertador_periodoAcademico", on_delete=models.RESTRICT, null=True,blank=True)
    malla= models.ManyToManyField(Malla,related_name= "ofertador_malla", null=True, blank=True)#1a muchos
    
    def __str__(self):
        return self.nombreOfertador

class horasHorario(models.Model):
    nombreHora = models.CharField(verbose_name= "nombreHora", max_length=50)
    dia =  models.DateField(verbose_name = "dia",max_length=50)
    horaInicio = models.TimeField(verbose_name="horaInicio",null=True, blank=True)
    horaFin = models.TimeField(verbose_name="horaFin",null=True, blank=True)
    
    def __str__(self):
        return self.nombreHora

class Horario(models.Model):
    nombreHorario =models.CharField(verbose_name="nombreHorario", max_length=100)
    aulas = models.ManyToManyField(Aulas,related_name= "materia_aulas", )#1a muchos
    materia = models.ManyToManyField(Materia,related_name= "materia_aulas", null=True, blank=True)
    horario = models.ManyToManyField(horasHorario,related_name= "aulas_horario", null=True, blank=True)
    
    def __str__(self):
        return self.nombreHorario 

class materia_horario(models.Model):
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE,null=True,blank=True)
    horario = models.ManyToManyField(Horario,related_name= "materia_horario", null=True, blank=True)
    horaInicio = models.TimeField(verbose_name ="horaInicio", null=True, blank=True)
    horaFin = models.TimeField(verbose_name ="horaFin", null=True, blank=True)
    Paralelo= models.ManyToManyField(Paralelo,related_name= "aulas_paralelo", null=True, blank=True)
    
    def __str__(self):
        return self.materia.nombreMateria
    
class materia_estudiante(models.Model):

    materia = models.ManyToManyField(Materia,related_name= "materia_estudiante",null=True,blank=True)
    estudiante = models.ManyToManyField(Estudiante,related_name= "materia_estudiante", null=True, blank=True)
    choices_materiaAprobada = [('s','Si'),('N','No'),('Sin','Sin Cursar')]
    materiaAprobada = models.CharField(verbose_name = "materiaAprobada",max_length=50,choices= choices_materiaAprobada)