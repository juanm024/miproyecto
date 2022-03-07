from datetime import date
from re import template
from django.http import HttpResponse
import random

from django.template import Context, Template, loader

def inicio(request):
    return HttpResponse("Hola, soy la nueva pagina")

def otravista(request):
    return HttpResponse("<H1>Sale pagina con mega titulo</H1>")

def numero_random(request):
    numero = random.randrange(15, 180)
    texto = "<H3>Este es tu numero aleatorio:", numero, "</H3>"
    return HttpResponse(texto)

def numero_usuario(request, numero):
    texto = "<H3>Este es tu numero: ", numero, "</H3>"
    return HttpResponse(texto)

def nacimiento(request, numero):
    nac = 2022 - numero
    texto = "<H3>Tu año de nacimiento es ", nac, "</H3>"
    return HttpResponse(texto)


def mi_plantilla(request):
    #plantilla = open(r"C:\Users\Juanm\Desktop\miproyecto\miproyecto\plantillas\mi_plantilla.html")
    #template = Template (plantilla.read())
    # context = Context(diccionario_datos) ----------- Copiar ubicacion plantillas en settings y todo remplazado por:
    
    template = loader.get_template("mi_plantilla.html")
    
    nombre = "Jorge"
    apellido = "Perez"

    lista = [3,1,2,45,7,23]

    diccionario_datos = {
        "nombre": nombre,
        "apellido": apellido,
        "nombre_largo": len(nombre),
        "lista": lista
    }
    plantilla_preparada = template.render(diccionario_datos)
    return HttpResponse(plantilla_preparada)
