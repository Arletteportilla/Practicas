# Generated by Django 4.2.3 on 2023-07-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "administrador",
            "0003_aulas_carrera_ciclo_coordinador_facultad_horario_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="malla",
            name="materias",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="malla_materia",
                to="administrador.materia",
            ),
        ),
    ]
