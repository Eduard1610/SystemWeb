from django.urls import path
from . import views
from .views import CategoriesCreateView

urlpatterns = [
    path('', views.categories, name='categories'),
    path('api/create/', CategoriesCreateView.as_view()),
]