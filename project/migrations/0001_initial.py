# Generated by Django 3.1.7 on 2021-05-08 19:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0002_auto_20210508_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project_type', models.CharField(max_length=50)),
                ('yearly_program', models.IntegerField()),
                ('initial_date', models.DateField(default=datetime.datetime(2021, 5, 8, 19, 16, 19, 546493))),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]