from django.shortcuts import render, HttpResponse
from tienda.models import Ciudades
#from ServiciosApp.models import Servicio
# Create your views here.


def home(request):

	return render(request, "ProyectoWebApp/home.html")


def busqueda_productos(request):

	if request.method == "POST":

		return render(request, "gracias.html")

	return render(request, "busqueda_productos.html")




def buscar(request):

	if request.GET["prd"]:
		#mensaje = "Articulo buscado: %r" %request.GET["prd"]
		nombre_ingresado = request.GET["prd"]

		if len(nombre_ingresado) < 30:

			ciudades = Ciudades.objects.filter(nombre__icontains=nombre_ingresado)  #este comando sirve para filtrar la base de datos

			return render(request, "resultados_busqueda.html", {"ciudades": ciudades, "query": nombre_ingresado})
		else:

			mensaje = "El texto ingresado es demasiado extenso"

	else:
		mensaje = "No has introducido nada"

	return HttpResponse(mensaje)

