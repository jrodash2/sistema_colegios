from django.forms import ModelForm
from .models import Calificacion
from django.forms import *



class CalificacionForm(ModelForm):
    class Meta:
        model = Calificacion 
        fields = ['carrera', 'grado', 'curso', 'docente', 'estudiante', 'usuario', 'activo', 'mark_1', 'mark_2', 'mark_3', 'mark_4', 'average']
        labels = {'carrera': 'Carreras ', 'grado': 'Grado', 'curso': 'Curso', 'docente': 'Docente', 'estudiante': 'Estudiante', 'usuario': 'Usuario', 'activo': 'Activo', 'mark_1': 'Nota 1', 'mark_2': 'Nota 2', 'mark_3': 'Nota 3', 'mark_4': 'Nota 4', 'average': 'Promedio'}
        widgets = {'carrera':  Select( attrs={'class': 'form-control'}), 'grado':  Select( attrs={'class': 'form-control'}), 'curso':  Select( attrs={'class': 'form-control'}),'docente':  Select( attrs={'class': 'form-control'}), 'estudiante':  Select( attrs={'class': 'form-control'}), 
                   'usuario':  Select( attrs={'class': 'form-control'}), 'activo':  CheckboxInput( attrs={'class': 'form-check-input'}),
                   'mark_1':  NumberInput( attrs={'class': 'form-control'}), 'mark_2':  NumberInput( attrs={'class': 'form-control'}), 'mark_3':  NumberInput( attrs={'class': 'form-control'}), 'mark_4':  NumberInput( attrs={'class': 'form-control'}), 'average':  NumberInput( attrs={'class': 'form-control', })}