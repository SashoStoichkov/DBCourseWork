from django.db import models
from django.utils import timezone

from project.models import Project

# Create your models here.
class Help(models.Model):
    date = models.DateField(default=timezone.now)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return 'Консултация за ' + str(self.project)
