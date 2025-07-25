# Generated by Django 5.1.5 on 2025-06-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0013_alter_rate_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='diabetes_type',
            field=models.CharField(blank=True, choices=[('1', '1-го типа'), ('2', '2-го типа'), ('mody', 'MODY-диабет'), ('gestational', 'Гестационный диабет'), ('many_types', 'Несколько типов диабета'), ('no_diabetes', 'Не болею диабетом')], default='', max_length=20, verbose_name='Тип диабета'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='treatment_type',
            field=models.CharField(blank=True, choices=[('insulin_therapy', 'Инсулинотерапия'), ('preparations', 'Препараты'), ('not_set', 'Не указывать')], default='', max_length=20, verbose_name='Тип лечения'),
        ),
    ]
