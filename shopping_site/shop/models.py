

from django.db import models

class Hospital(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fname} {self.lname}"

