from django import forms
from .models import Selection, Teacher


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ['teacher', 'email', 'student_name', 'tier']
        labels = {
            'email': 'Seu Email',
            'student_name': 'Seu Nome Completo',
            'tier': 'Sua Turma',
            'teacher': 'Professor Desejado'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'tier': forms.Select(attrs={'class': 'form-select'}),
            'teacher': forms.Select(attrs={'class': 'form-select'})
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@aluno.ce.gov.br'):
            raise forms.ValidationError('O email deve terminar com @aluno.ce.gov.br.')
        if Selection.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um registro com esse email.')
        return email
    
    def clean_student_name(self):
        student_name = self.cleaned_data.get('student_name')
        if len(student_name) < 8:
            raise forms.ValidationError('O nome deve ter pelo menos 8 caracteres.')
        return student_name
    
    def clean_tier(self):
        tier = self.cleaned_data.get('tier')
        if tier not in dict(Selection.TIER_CHOICES):
            raise forms.ValidationError('Turma inválida.')
        return tier
    
    def clean_teacher(self):
        teacher = self.cleaned_data.get('teacher')
        if not teacher:
            raise forms.ValidationError('Selecione um professor.')
        if Selection.objects.filter(teacher=teacher).count() >= 9:
            raise forms.ValidationError('Este professor já foi escolhido pelo limite máximo de alunos. (9 alunos)')
        return teacher
