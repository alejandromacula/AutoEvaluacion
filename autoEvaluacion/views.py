# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView


def newPregunta(request):
	return render_to_response('nueva_pregunta.html', {})

def newAsignatura(request):
	return render_to_response('nueva_asignatura.html', {})

def newExamen(request):
	return render_to_response('nuevo_examen.html', {})
