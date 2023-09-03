# Generated by Django 4.2.3 on 2023-07-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrador", "0004_aulas_modalidad"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aulas",
            name="modalidad",
        ),
        migrations.AddField(
            model_name="docente",
            name="limiteHoras",
            field=models.IntegerField(
                blank=True, max_length=50, null=True, verbose_name="limiteHoras"
            ),
        ),
    ]
