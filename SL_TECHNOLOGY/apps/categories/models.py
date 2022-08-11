from django.db import models

# Create your models here.
class Categories(models.Model):
    nombre_categoria = models.CharField(max_length=70)

    