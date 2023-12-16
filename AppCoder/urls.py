"""
URL configuration for ProyectoCoder47785 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import crear_curso, show_html, mostrar_cursos, crear_curso_form, busqueda_camada, CursoList, \
    CursoDetalle, CursoCreacion, CursoActualizacion, CursoEliminar

urlpatterns = [
    path("AddCurso/",crear_curso),
    path("ShowPage/", show_html),
    path('Cursos/',mostrar_cursos),
    path('FormCurso/',crear_curso_form),
    path('BuscaCurso/',busqueda_camada),
    path('cursosListar/',CursoList.as_view(), name="List"),
    path('curso/<int:pk>',CursoDetalle.as_view(), name="CursoDetail"),
    path('crear/', CursoCreacion.as_view(), name="CursoCreate"),
    path('editar/<int:pk>', CursoActualizacion.as_view(), name="CursoEditar"),
    path('eliminar/<int:pk>', CursoEliminar.as_view(), name="CursoEliminar"),
]
