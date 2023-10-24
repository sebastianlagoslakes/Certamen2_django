# Generated by Django 4.2.6 on 2023-10-22 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_comunicado_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='tipo',
            field=models.CharField(choices=[('S', 'Suspension de actividades'), ('C', 'Suspension de clase'), ('I', 'Informacion')], default='I', max_length=1),
        ),
    ]
