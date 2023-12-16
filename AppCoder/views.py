from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from AppCoder.forms import CursoForm, BusquedaCursoForm
from AppCoder.models import Curso
# Create your views here.

class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_1.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/app/cursosListar"
    template_name = "AppCoder/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoActualizacion(UpdateView):
    model = Curso
    success_url = "/app/cursosListar"
    template_name = "AppCoder/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoEliminar(DeleteView):
    model = Curso
    template_name = "Appcoder/eliminar_curso.html"
    success_url = "/app/cursosListar"







def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos" : cursos,
        "form": BusquedaCursoForm(),
    }
    #return redirect("/app/AddCurso/")
    return render(request,"AppCoder/Cursos.html", contexto )

def crear_curso(request):
    curso = Curso(nombre="Python", camada=472473)
    curso.save()
    contexto = {"curso":curso}
    return redirect("/app/Cursos/")

def crear_curso_form(request):
    if request.method == "POST":
        curso_formulario = CursoForm(request.POST) #Esto llena el formulario
        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            curso_crear = Curso(nombre = informacion["nombre"], camada = informacion["camada"])
            curso_crear.save()
            return redirect("/app/Cursos/")

    curso_formulario = CursoForm()
    contexto = {
        "form":curso_formulario
    }
    return render(request, "AppCoder/crear_curso.html", contexto)

def busqueda_camada(request):
    nombre = request.GET["nombre"]
    cursos = Curso.objects.filter(nombre__icontains=nombre)
    contexto = {
        "cursos": cursos,
        "form": BusquedaCursoForm(),
    }
    # return redirect("/app/AddCurso/")
    return render(request, "AppCoder/Cursos.html", contexto)



def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso":curso, "nombre": "Jose"}
    return render(request,"index.html",contexto)


