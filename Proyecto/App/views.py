from django.shortcuts import render
from django.http import HttpResponse
from App.models import Medico, Paciente, Especialidad
from App.forms import MedicoForm, PacienteForm, EspecialidadForm

# Create your views here.
def inicio(request):
    return render(request, "App/index.html")

def medicos(request):
    return render(request, "App/medicos.html")

def pacientes(request):
    return render(request, "App/pacientes.html")

def especialidades(request):
    return render(request, "App/especialidades.html")



def medicoForm(request):
    if request.method == 'POST':
        miFormulario = MedicoForm(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Medico(nombre = info['nombre'], apellido = info['apellido'], matricula = info['matricula'])
            info.save()
            return render(request, 'App/index.html')
    else:
        miFormulario = MedicoForm()
    return render(request, "App/medicoForm.html",{'miFormulario':miFormulario})


def pacienteForm(request):
    if request.method == 'POST':
        miFormulario = PacienteForm(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Paciente(nombre = info['nombre'], apellido = info['apellido'], email = info['email'], dni = info['dni'])
            info.save()
            return render(request, 'App/index.html')
    else:
        miFormulario = PacienteForm()
    return render(request, "App/pacienteForm.html",{'miFormulario':miFormulario})


def especialidadForm(request):
    if request.method == 'POST':
        miFormulario = EspecialidadForm(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Especialidad(nombre = info['nombre'], descripcion = info['descripcion'], codigo = info['codigo'])
            info.save()
            return render(request, 'App/index.html')
    else:
        miFormulario = EspecialidadForm()
    return render(request, "App/especialidadForm.html",{'miFormulario':miFormulario})
