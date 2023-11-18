from django.urls import path
from Inicio.views import inicio, produ, hacer_pedido, ingreso, promo, eliminar, actualizar, detalle, acerca


urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('Produ/', produ, name = 'productos'),
    path('Produ/pedir/', hacer_pedido, name = 'pedidos'),
    path('clientes/', ingreso ,name = 'clientes'),
    path('promociones/', promo ,name = 'promos'),
    path('Produ/<int:Productos_id>/eliminar/', eliminar, name = 'eliminar_productos'),
    path('Produ/<int:Productos_id>/actualizar/', actualizar, name = 'actualizar_productos'),
    path('Produ/<int:Productos_id>/detalle/', detalle , name = 'detalle_productos'),
    path('acerca/', acerca ,name = 'acerca')
]
