# Generated by Django 4.1.2 on 2022-10-16 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
    ]
