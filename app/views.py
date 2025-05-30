# app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'app/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            stock=request.POST['stock']
        )
        return redirect('lista_productos')
    return render(request, 'app/crear.html')

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.stock = request.POST['stock']
        producto.save()
        return redirect('lista_productos')
    return render(request, 'app/editar.html', {'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    return redirect('lista_productos')
