from django.http import HttpResponse
from django.shortcuts import render
from clase.forms import BusquedaCurso, CursoFormulario
from clase.models import Curso
import random

# Create your views here.

def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre= "Curso JS", camada=camada)
    nuevo_curso.save()
    return HttpResponse("Se creo el curso", nuevo_curso.nombre, "camada", camada)


def formulario_curso(request):

#Sin formularios de django
    #print(request.method)
    #if request.method == "POST":
    #    print(request.POST)
    #    nuevo_curso = Curso(nombre= request.POST["curso"], camada= request.POST["camada"])
    #    nuevo_curso.save()
    #    return render(request, "clase/formulario_curso.html", {"nuevo_curso": nuevo_curso}) #este por si viene por POST

    #return render(request, "clase/formulario_curso.html", {})


#Con formulario django:
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Curso(nombre= data["curso"], camada= data["camada"])
            nuevo_curso.save()
            return render(request, "indice/index.html", {"nuevo_curso": nuevo_curso})
    
    formulario = CursoFormulario()
    return render(request, "clase/formulario_curso.html", {"formulario": formulario})


def busqueda_curso(request):

    request.GET.get("partial_curso", None)

    buscador = BusquedaCurso()
    return render(request, "clase/busqueda_curso.html", {"buscador": buscador})