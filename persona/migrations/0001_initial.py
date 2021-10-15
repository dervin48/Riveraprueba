# Generated by Django 3.2.2 on 2021-09-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='tipo telefono')),
            ],
            options={
                'verbose_name': 'Tipo Telefono',
                'verbose_name_plural': 'Tipos de Telefono',
                'db_table': 'tipo_telefono',
            },
        ),
    ]