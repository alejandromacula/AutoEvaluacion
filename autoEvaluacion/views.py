# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return render_to_response('index.html', {'username':request.user.username})

@login_required
def newPregunta(request):
	return render_to_response('nueva_pregunta.html', {})

@login_required
def newAsignatura(request):
	return render_to_response('nueva_asignatura.html', {})

@login_required
def newExamen(request):
	return render_to_response('nuevo_examen.html', {})

@login_required
def administrador(request):
	return render_to_response('administrador.html', {})
