# Generated by Django 4.0.5 on 2022-07-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
