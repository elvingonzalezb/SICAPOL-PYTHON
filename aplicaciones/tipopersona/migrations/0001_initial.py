# Generated by Django 2.2.5 on 2020-05-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipopersona',
            fields=[
                ('cod_tip_per', models.AutoField(primary_key=True, serialize=False)),
                ('tip_per', models.CharField(max_length=250)),
                ('usuario', models.CharField(max_length=30)),
                ('opc_car', models.CharField(max_length=4)),
                ('fec_car', models.DateField(auto_now=True)),
                ('hor_car', models.DateField(auto_now=True)),
                ('elimina', models.CharField(max_length=2)),
            ],
        ),
    ]
