# Generated by Django 4.2.6 on 2024-03-14 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturacolegiatura',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='facturacolegiatura',
            name='items',
        ),
        migrations.DeleteModel(
            name='DetalleFactura',
        ),
        migrations.DeleteModel(
            name='FacturaColegiatura',
        ),
        migrations.DeleteModel(
            name='ItemFactura',
        ),
    ]
