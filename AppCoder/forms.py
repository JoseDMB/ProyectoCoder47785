from django import forms

class CursoForm(forms.Form):
    titulo = forms.CharField()
    blog = forms.CharField()
    imagen = forms.ImageField()


class BusquedaCursoForm(forms.Form):
    nombre = forms.CharField()
