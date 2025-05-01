from django.db import models
from teachers.models import Teacher


class Selection(models.Model):
    student_name = models.CharField(max_length=255, verbose_name='Nome do Estudante')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='selections', verbose_name='Horário')

    def __str__(self):
        return f"{self.student_name} - {self.teacher.name}"
    
    class Meta:
        verbose_name = 'Seleção'
        verbose_name_plural = 'Seleções'
