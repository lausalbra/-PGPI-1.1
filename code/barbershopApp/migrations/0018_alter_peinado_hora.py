# Generated by Django 4.1.3 on 2022-12-07 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershopApp', '0017_alter_barba_hora_alter_cortes_hora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peinado',
            name='hora',
            field=models.DateTimeField(error_messages={'invalid': '“%(value)s” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.', 'invalid_date': '“%(value)s” value has the correct format (YYYY-MM-DD) but it is an invalid date.', 'invalid_datetime': '“%(value)s” value has the correct format (YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]) but it is an invalid date/time.'}, help_text='Año-Mes-Dia Hora:Minuto'),
        ),
    ]
