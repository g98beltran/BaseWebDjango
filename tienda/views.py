from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.
def products_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/products_list.html', {'productos': productos})

def descripcion(request, pk):
    productos = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/descripcion.html', {'productos': productos})