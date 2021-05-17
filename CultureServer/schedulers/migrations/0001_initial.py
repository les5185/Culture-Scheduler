# Generated by Django 3.2.3 on 2021-05-17 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('title', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
