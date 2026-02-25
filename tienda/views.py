from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = list(Producto.objects.all())
    productos_ordenados = sorted(productos, key=lambda x: x.precio)
    return render(request, 'lista.html', {'productos': productos_ordenados})