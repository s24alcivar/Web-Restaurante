from django.shortcuts import render, redirect
from .models import Project

# Create your views here.
def home(request):
    projectopepe = Project.objects.all()
    return render(request, "core/base.html", {"projecto": projectopepe})
def contacto(request):
    return render(request, 'core/base.html')

def crearContacto(request):
    nombres=request.POST['txtNombres']
    correo_electronico=request.POST['txtCorreo']
    asunto=request.POST['txtAsunt']
    mensaje=request.POST['txtMensaje']

    proyectos = Project.objects.create(
        nombres=nombres, correo_electronico=correo_electronico, asunto=asunto, mensaje=mensaje)
    proyectos.save()
    return redirect('/')

def edicionContacto(request, nombres):
    proyectos = Project.objects.get(nombres=nombres)
    return render(request, 'edicionContacto.html', {'proyectos': proyectos})

def editarContacto(request, nombres):
    nombres=request.POST['txtNombres']
    correo_electronico=request.POST['txtCorreo']
    asunto=request.POST['txtAsunt']
    mensaje=request.POST['txtMensaje']

    proyectos = Project.objects.get(nombres=nombres)
    proyectos.correo_electronico = correo_electronico
    proyectos.asunto = asunto
    proyectos.mensaje = mensaje
    proyectos.save()

    return redirect('/')
   

def eliminarContacto(request, nombres):
    proyectos = Project.objects.get(nombres=nombres)
    proyectos.delete()

    return redirect('/')