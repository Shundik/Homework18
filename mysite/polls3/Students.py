from django.db import models


class SStudents(models.Model):
    first_name = models.CharField(max_length=256)
    second_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.first_name)


# Create your models here.
