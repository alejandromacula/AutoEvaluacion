from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class examen(models.Model):
    tipo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
