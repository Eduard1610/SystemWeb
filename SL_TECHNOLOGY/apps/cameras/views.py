from .models import Cameras
from .serializers import CamerasSerializer
from rest_framework import generics
from django.shortcuts import render

class CamerasCreateView(generics.ListCreateAPIView):
    queryset = Cameras.objects.all()
    serializer_class = CamerasSerializer

# Create your views here.
def cameras(request):
    return render(request, 'cameras.html')
