from django.shortcuts import render
from tienda.models import Ciudades, AtractivosTuristicos

# Create your views here.
def tienda(request):
	ciudades=Ciudades.objects.all()
	turistico=AtractivosTuristicos.objects.all()
	return render(request, "tienda/tienda.html", {"ciudades": ciudades, "turistico": turistico})