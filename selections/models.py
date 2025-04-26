from django.db import models
from teachers.models import Teacher


class Selection(models.Model):
    student_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='selections')

    def __str__(self):
        return f"{self.student_name} - {self.teacher.name}"
