from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.
def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    curso.save()
    return HttpResponse(f"El curso es {curso.nombre} y el número de camada es {curso.camada}")
