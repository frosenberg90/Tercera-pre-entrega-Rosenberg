from django.urls import path
from Inicio.views import inicio, produ, hacer_pedido

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('Produ/', produ, name = 'productos'),
    path('Produ/pedir/', hacer_pedido, name = 'pedidos'),
    path('clientes/', hacer_pedido, name = 'clientes')
]
