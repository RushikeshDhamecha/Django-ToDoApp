# Generated by Django 4.2.2 on 2023-06-25 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Desc',
            new_name='addDesc',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Title',
            new_name='addTitle',
        ),
    ]
