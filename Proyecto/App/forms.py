from django import forms

class MedicoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    matricula = forms.IntegerField(max_value=999999)
    
    
class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    dni = forms.IntegerField(max_value=99999999)

class EspecialidadForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    codigo = forms.IntegerField(max_value=9999)