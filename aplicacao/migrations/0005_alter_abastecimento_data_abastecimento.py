# Generated by Django 5.0.7 on 2024-08-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0004_alter_abastecimento_data_abastecimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abastecimento',
            name='data_abastecimento',
            field=models.DateTimeField(unique=True),
        ),
    ]
