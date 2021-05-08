from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from project.models import Project

# Create your models here.
class Exam(models.Model):
    date = models.DateField(default=timezone.now)

    grade_validator = [MinValueValidator(2.00), MaxValueValidator(6.00)]

    grade_1 = models.FloatField(validators=grade_validator)
    grade_2 = models.FloatField(validators=grade_validator)
    grade_3 = models.FloatField(validators=grade_validator)
    grade_4 = models.FloatField(validators=grade_validator)
    grade_5 = models.FloatField(validators=grade_validator)

    avg_grade = models.FloatField(validators=grade_validator)

    final_grade = models.FloatField(validators=grade_validator)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return 'Защита на ' + self.project
