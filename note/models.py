from django.db import models
from student.models import Student

# Create your models here.
class Note(models.Model):
    note = models.TextField()

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return 'Бележка за ' + self.student.get_full_name()
