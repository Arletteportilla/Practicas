# Generated by Django 4.2.3 on 2023-07-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrador", "0003_paralelo_materia"),
    ]

    operations = [
        migrations.AddField(
            model_name="aulas",
            name="modalidad",
            field=models.CharField(
                blank=True,
                choices=[("V", "Virtual"), ("P", "Presencial")],
                max_length=50,
                null=True,
                verbose_name="modalidad",
            ),
        ),
    ]