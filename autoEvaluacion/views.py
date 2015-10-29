# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
	return render_to_response('blank.html', {})

def login(request):
	return render_to_response('login.html', {})

def newPregunta(request):
	return render_to_response('nueva_pregunta.html', {})