# Generated by Django 4.2 on 2023-10-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='image',
            field=models.ImageField(upload_to='stuff/', verbose_name='Stuff Image'),
        ),
    ]