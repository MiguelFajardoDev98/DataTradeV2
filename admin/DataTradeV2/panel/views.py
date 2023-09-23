from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inventario

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")

def listar(request):
    listaproductos = Inventario.objects.all()
    datoslistaproductos = {'productos':listaproductos}
    return render(request, "crud_inventario/listar.html", datoslistaproductos)

def agregar(request):
    if request.method == "POST":
        print("Datos del formulario:", request.POST)
        if (
            request.POST.get('nombreProducto') and
            request.POST.get('valorUnidad') and
            request.POST.get('cantidadProducto') 
        ):
            producto = Inventario()
            producto.nombreProducto = request.POST.get('nombreProducto')
            producto.valorUnidad = request.POST.get('valorUnidad')
            producto.cantidadProducto = request.POST.get('cantidadProducto')
            producto.save()
            return redirect('listar') 
        else:
            return HttpResponse("Faltan datos en el formulario", status=400)  # Respuesta de error si faltan datos
    else:
        return render(request, "crud_inventario/agregar.html")

def actualizar(request):
    return render(request, "crud_inventario/actualizar.html")

def eliminar(request):
    return render(request, "crud_inventario/eliminar.html")