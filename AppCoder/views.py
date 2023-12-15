from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Curso
# Create your views here.


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos" : cursos
    }
    #return redirect("/app/AddCurso/")
    return render(request,"AppCoder/Cursos.html", contexto )

def crear_curso(request):
    curso = Curso(nombre="Python", camada=472473)
    curso.save()
    contexto = {"curso":curso}
    return redirect("/app/Cursos/")

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso":curso, "nombre": "Jose"}
    return render(request,"index.html",contexto)