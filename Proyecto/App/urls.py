from django.urls import path
from App.views import *

urlpatterns = [
    #URLs principales
    path('', inicio, name="home"),
    path('medicos/', medicos, name="medicos"),
    path('pacientes/', pacientes, name="pacientes"),
    path('especialidades/', especialidades, name='especialidades'),
    
    #URLs formularios
    path('medicoForm/',medicoForm, name='medicoForm'),
    path('pacienteForm/',pacienteForm, name='pacienteForm'),
    path('especialidadForm/',especialidadForm, name='especialidadForm'),
]