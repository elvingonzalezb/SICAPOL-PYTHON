# Generated by Django 2.2.5 on 2020-05-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipopersona', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipopersona',
            old_name='cod_tip_per',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='tipopersona',
            name='tip_per',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
