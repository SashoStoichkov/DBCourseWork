from django.utils import timezone
from django.db import models

from student.models import Student

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    project_type = models.CharField(max_length=50)
    yearly_program = models.IntegerField()
    initial_date = models.DateField(default=timezone.now)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' на ' + self.student.get_full_name()
