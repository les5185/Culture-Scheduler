# Generated by Django 3.2.3 on 2021-05-17 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='compainion',
            new_name='companion',
        ),
    ]