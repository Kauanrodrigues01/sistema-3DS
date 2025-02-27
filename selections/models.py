from django.db import models
from teachers.models import Teacher


class Selection(models.Model):
    TIER_CHOICES = [
        ('3A', '3º Administração'),
        ('3DS', '3º Desenvolvimento de Sistemas'),
        ('3E', '3º Enfermagem'),
        ('3I', '3º Informática'),
        # ('3L', '3º Logística'),
    ]
    email = models.EmailField(unique=True)
    student_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True)
    tier = models.CharField(max_length=3, choices=TIER_CHOICES)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='selections')

    def __str__(self):
        return f"{self.student_name} - {self.teacher.name} - {self.tier}"
