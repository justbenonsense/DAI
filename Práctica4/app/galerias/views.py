from django.shortcuts import render, redirect
from .models import Galeria, Cuadro
from .forms import GaleriaForm, CuadroForm


def index(request):
    return render(request, 'index.html', {})

def listaCuadros(request):
    cuadros = Cuadro.objects.all().order_by('nombre')
    return render(request, 'lista_cuadros.html', {'cuadros':cuadros})

def insertarCuadro(request):
    error = None
    if request.method == "POST":
        form = CuadroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cuadros')
        else:
            error = form.errors
    else:
        form = CuadroForm()
    return render(request, 'insertar_cuadro.html', {'form':form, 'error':error})


def modificarCuadro(request, pk):
    error = None
    cuadro = Cuadro.objects.get(nombre=pk)
    if request.method == "POST":
        form = CuadroForm(request.POST, request.FILES, instance=cuadro)
        if form.is_valid():
            form.save()
            return redirect('lista_cuadros')
        else:
            error = form.errors
    else:
        form = CuadroForm(instance=cuadro)
    return render(request, 'modificar_cuadro.html', {'form':form, 'error':error})
   

def eliminarCuadro(request, pk):
    cuadro = Cuadro.objects.get(nombre=pk)
    
    if request.method == "POST":
        cuadro.delete()
        return redirect('lista_cuadros')
    
    return render(request, 'eliminar_cuadro.html', {'cuadro':cuadro})

def listaGalerias(request):
    galerias = Galeria.objects.all().order_by('nombre')
    return render(request, 'lista_galerias.html', {'galerias':galerias})

def insertarGaleria(request):
    error = None
    if request.method == "POST":
        form = GaleriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_galerias')
        else:
            error = form.errors
    else:
        form = GaleriaForm()
    return render(request, 'insertar_galeria.html', {'form': form, 'error':error})

def modificarGaleria(request, pk):
    error = None
    galeria = Galeria.objects.get(nombre=pk)
    if request.method == "POST":
        form = GaleriaForm(request.POST, instance=galeria)
        if form.is_valid():
            form.save()
            return redirect('lista_galerias')
        else:
            error = form.errors
    else:
        form = GaleriaForm(instance=galeria)
    return render(request, 'modificar_galeria.html', {'form':form, 'error':error})

def eliminarGaleria(request, pk):
    galeria = Galeria.objects.get(nombre=pk)
    
    if request.method == "POST":
        galeria.delete()
        return redirect('lista_galerias')
    
    return render(request, 'eliminar_galeria.html', {'galeria':galeria})
