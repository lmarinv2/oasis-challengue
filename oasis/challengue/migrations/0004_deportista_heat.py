# Generated by Django 4.0.6 on 2022-11-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challengue', '0003_remove_deportista_puntos_remove_wod_puntos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deportista',
            name='Heat',
            field=models.IntegerField(null=True),
        ),
    ]
