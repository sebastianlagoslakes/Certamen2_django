# Generated by Django 4.2.6 on 2023-10-21 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_entidad_remove_docente_carrera_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='fecha_actual',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
