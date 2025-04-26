from django import forms
from .models import Selection, Teacher
import re


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ['teacher', 'student_name',]
        labels = {
            'student_name': 'Seu Nome Completo',
            'teacher': 'Horário Desejado',
        }
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'teacher': forms.Select(attrs={'class': 'form-select'})
        }
    
    def clean_student_name(self):
        student_name = self.cleaned_data.get('student_name')
        if len(student_name) < 8:
            raise forms.ValidationError('O nome deve ter pelo menos 8 caracteres.')
        return student_name
    
    def clean_teacher(self):
        teacher = self.cleaned_data.get('teacher')
        if not teacher:
            raise forms.ValidationError('Selecione um professor.')
        if Selection.objects.filter(teacher=teacher).count() >= teacher.available_quantity:
            raise forms.ValidationError(f'Este horário já foi escolhido pelo limite máximo de alunos. ({teacher.available_quantity} alunos)')
        return teacher
