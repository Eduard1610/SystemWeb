from django.db import models

# Create your models here.
class Cameras(models.Model):
    nombre_camara = models.CharField(max_length=70)