# Generated by Django 4.2 on 2023-10-10 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_stuff_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stuff',
            new_name='Staff',
        ),
    ]