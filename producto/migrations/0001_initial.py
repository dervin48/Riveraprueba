# Generated by Django 3.2.2 on 2021-09-23 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='marca')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproducto', models.CharField(max_length=14, verbose_name='Id Producto')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='precio')),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='precio costo')),
                ('existencia', models.IntegerField(verbose_name='existencia')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.marca', verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
    ]
