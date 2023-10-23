# Generated by Django 4.2 on 2023-10-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reservation_date_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Choose a day'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='Choose a Time'),
        ),
    ]
