from django.urls import path
from .views import inicio, otravista, numero_random, numero_usuario, nacimiento, mi_plantilla

urlpatterns = [
    path("", inicio),
    path("otravista/", otravista),
    path("numero_random/", numero_random),
    path("numero_usuario/<int:numero>", numero_usuario),
    path("nacimiento/<int:numero>", nacimiento),
    path("mi_plantilla/", mi_plantilla)
]