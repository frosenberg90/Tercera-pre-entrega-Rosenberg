from django.urls import path
from Ensaladas.views import ListadoEnsaladas, CrearEnsaladas, ActualizarEnsaladas, EliminarEnsaladas, DetalleEnsaladas

urlpatterns = [
    path('Ensaladas/', ListadoEnsaladas.as_view(), name='ensaladas'),
    path('Ensaladas/crear/', CrearEnsaladas.as_view(), name='crear_ensaladas'),
    path('Ensaladas/<int:pk>/', DetalleEnsaladas.as_view(), name='detalle_ensaladas'),
    path('Ensaladas/<int:pk>/actualizar/', ActualizarEnsaladas.as_view(), name='actualizar_ensaladas'),
    path('Ensaladas/<int:pk>/eliminar/', EliminarEnsaladas.as_view(), name='eliminar_ensaladas'),
]