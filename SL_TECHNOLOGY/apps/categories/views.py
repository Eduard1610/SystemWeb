from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework import generics
from django.shortcuts import render

class CategoriesCreateView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

# Create your views here.
def categories(request):
    return render(request, 'categories.html')
