from django.shortcuts import render
from django.http import HttpResponse
from .models import deportista
# Create your views here.

def home(request):
    return render(request,'home.html')

def pagina(request):
    dep = []
    if request.method == "POST":
        genero = request.POST.get("genero")
        categoria = request.POST.get("categoria")
        #usuario = deportista.objects.values_list('Genero','Categoria',"Nombre_apellidos","Puntos")
        dep = deportista.objects.filter(Genero=genero,Categoria=categoria)

    return render(request,'resultados.html',{'dep':dep})