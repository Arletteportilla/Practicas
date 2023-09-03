from rest_framework import serializers
from .models import Docente,Estudiante, Coordinador, Carrera, Facultad, Malla, Ciclo, Ofertador, PeriodoAcademico, Materia, Aulas, Paralelo, Horario, materia_estudiante, Funciones, horasHorario


class DocenteSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class EstudianteSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class CoordinadorSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'

class CarreraSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class FacultadSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class MallaSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Malla
        fields = '__all__'

class CicloSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Ciclo
        fields = '__all__'

class OfertadorSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Ofertador
        fields = '__all__'

class PeriodoAcademicoSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = '__all__'

class MateriaSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

class AulasSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Aulas
        fields = '__all__'

class ParaleloSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Paralelo
        fields = '__all__'

class HorarioSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class materia_estudianteSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = materia_estudiante
        fields = '__all__'

class FuncionesSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Funciones
        fields = '__all__'

class horasHorarioSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = horasHorario
        fields = '__all__'
