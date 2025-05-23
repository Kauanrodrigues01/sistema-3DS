# Generated by Django 5.1.6 on 2025-04-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Horário', 'verbose_name_plural': 'Horários'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='available_quantity',
            field=models.PositiveIntegerField(verbose_name='Quantidade disponível'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
    ]
