# Generated by Django 4.0.6 on 2022-11-25 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deportistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_apellidos', models.CharField(max_length=40)),
                ('Genero', models.CharField(max_length=40)),
                ('puntos', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='wod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wod_numero', models.CharField(max_length=40)),
                ('puntos', models.CharField(blank=True, max_length=30, null=True)),
                ('Deportista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='challengue.deportistas')),
            ],
        ),
    ]
