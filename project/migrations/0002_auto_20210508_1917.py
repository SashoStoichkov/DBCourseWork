# Generated by Django 3.1.7 on 2021-05-08 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='initial_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
