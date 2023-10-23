# Generated by Django 4.2 on 2023-09-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('price', models.IntegerField()),
                ('time', models.IntegerField(verbose_name='Prepare Time')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Date of Release')),
                ('photo', models.ImageField(upload_to='foods/')),
            ],
        ),
    ]
