from django.shortcuts import render
from rest_framework import viewsets
from .serialices import DocenteSerialaizers, EstudianteSerialaizers, CoordinadorSerialaizers, CarreraSerialaizers, FacultadSerialaizers, MallaSerialaizers, CicloSerialaizers, OfertadorSerialaizers, PeriodoAcademicoSerialaizers, MateriaSerialaizers, AulasSerialaizers, ParaleloSerialaizers, HorarioSerialaizers, materia_estudianteSerialaizers,FuncionesSerialaizers, horasHorarioSerialaizers
from .models import Docente,Estudiante, Coordinador, Carrera, Facultad, Malla, Ciclo, Ofertador, PeriodoAcademico, Materia, Aulas, Paralelo, Horario, materia_estudiante, Funciones, horasHorario

# Create your views here.

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerialaizers

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerialaizers

class CoordinadorViewSet(viewsets.ModelViewSet):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerialaizers

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerialaizers

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerialaizers

class MallaViewSet(viewsets.ModelViewSet):
    queryset = Malla.objects.all()
    serializer_class = MallaSerialaizers

class CicloViewSet(viewsets.ModelViewSet):
    queryset = Ciclo.objects.all()
    serializer_class = CicloSerialaizers

class OfertadorViewSet(viewsets.ModelViewSet):
    queryset = Ofertador.objects.all()
    serializer_class = OfertadorSerialaizers

class PeriodoAcademicoViewSet(viewsets.ModelViewSet):
    queryset = PeriodoAcademico.objects.all()
    serializer_class = PeriodoAcademicoSerialaizers

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerialaizers

class AulasViewSet(viewsets.ModelViewSet):
    queryset = Aulas.objects.all()
    serializer_class = AulasSerialaizers

class ParaleloViewSet(viewsets.ModelViewSet):
    queryset = Paralelo.objects.all()
    serializer_class = ParaleloSerialaizers

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerialaizers

class materia_estudianteViewSet(viewsets.ModelViewSet):
    queryset = materia_estudiante.objects.all()
    serializer_class = materia_estudianteSerialaizers

class FuncionesViewSet(viewsets.ModelViewSet):
    queryset = Funciones.objects.all()
    serializer_class = FuncionesSerialaizers

class horasHorarioViewSet(viewsets.ModelViewSet):
    queryset = horasHorario.objects.all()
    serializer_class = horasHorarioSerialaizers
