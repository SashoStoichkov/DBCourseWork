# Generated by Django 3.1.7 on 2021-05-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='faculty_number',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]