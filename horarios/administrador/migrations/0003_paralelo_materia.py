# Generated by Django 4.2.3 on 2023-07-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrador", "0002_remove_materia_estudiante_materia_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="paralelo",
            name="materia",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                to="administrador.materia",
                verbose_name="materia",
            ),
        ),
    ]