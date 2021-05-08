from django.db import models

# Create your models here.
class Student(models.Model):
    faculty_number = models.BigAutoField(primary_key=True, unique=True)

    first_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    year = models.CharField(max_length=50)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' ( ' + self.year + ' )'

    def __str__(self):
        return self.get_full_name()
