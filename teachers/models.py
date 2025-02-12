from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teachers_photos/')

    def __str__(self):
        return self.name
