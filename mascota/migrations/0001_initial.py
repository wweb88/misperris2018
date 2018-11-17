# Generated by Django 2.0.9 on 2018-11-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('rescatado', 'Rescatado'), ('disponible', 'Disponible'), ('adoptado', 'Adoptado')], default='rescatado', max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
    ]