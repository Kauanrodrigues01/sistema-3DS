from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    available_quantity = models.PositiveIntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.name
