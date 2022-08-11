from django.urls import path
from .import views
from .views import CamerasCreateView

urlpatterns = [
    path('', views.cameras, name='cameras'),
    path('api/create/', CamerasCreateView.as_view()),
]
