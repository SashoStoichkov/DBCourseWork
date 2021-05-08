from django.db import models
from student.models import Student

# Create your models here.
class Study(models.Model):
    degree = models.CharField(max_length=50)
    form = models.CharField(max_length=50)
    group = models.IntegerField()

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.degree + ' ' + self.student.get_full_name()
