from rest_framework.serializers import ModelSerializer

from .models import Cameras

class CamerasSerializer(ModelSerializer):
    class Meta:
        model = Cameras
        fields = ('id','nombre_camara')