# book/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal para la vista "index"
]
