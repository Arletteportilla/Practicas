from django.contrib import admin 
from .models import Estudiante,Docente,Coordinador,Facultad,Carrera,Malla,Ciclo,Ofertador,PeriodoAcademico,Materia,Aulas,Paralelo,Horario

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Coordinador)
admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Malla)
admin.site.register(Ciclo)
admin.site.register(Ofertador)
admin.site.register(PeriodoAcademico)
admin.site.register(Materia)
admin.site.register(Aulas)
admin.site.register(Paralelo)
admin.site.register(Horario)