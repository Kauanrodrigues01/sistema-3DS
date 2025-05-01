from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    available_quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name='Quantidade disponível')
    
    def __str__(self):
        return f'{self.name} - {self.available_quantity} formandos'

    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'
