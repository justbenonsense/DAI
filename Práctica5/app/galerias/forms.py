from django import forms
from .models import Galeria, Cuadro

class GaleriaForm(forms.ModelForm):
    
    class Meta:
        model = Galeria 
        fields = ('nombre', 'dirección')


class CuadroForm(forms.ModelForm):
    
    class Meta:
        model = Cuadro 
        fields = ('nombre', 'galeria', 'autor', 'fecha_creación', 'imagen')