from django.shortcuts import render
from django.http import HttpResponse
from .models import deportista
# Create your views here.

def home(request):
    return render(request,'home.html')

def horarios(request):
    return render(request,'horarios.html')

def pagina(request):
    dep = []
    puntos()
    if request.method == "POST":
        genero = request.POST.get("genero")
        categoria = request.POST.get("categoria")
        #usuario = deportista.objects.values_list('Genero','Categoria',"Nombre_apellidos","Puntos")
        dep = deportista.objects.filter(Genero=genero,Categoria=categoria)
    

    return render(request,'resultados.html',{'dep':dep})

def puntos():
    puntos = deportista.objects.values_list('Nombre_apellidos','w1','w2','w3','w4')
    a=0;
    for i in puntos: 
        total=0;   
        print(puntos[a][1]) 
        print(puntos[a][0])     
        w1=puntos[a][1]
        w2=puntos[a][2]
        w3=puntos[a][3]
        w4=puntos[a][4]
        total = int(w1) +int(w2)+int(w3)+int(w4);
        deportista.objects.filter(Nombre_apellidos=puntos[a][0]).update(Puntos=total)
        a=a+1;