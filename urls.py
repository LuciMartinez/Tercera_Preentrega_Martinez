from django.urls import path
from views import listar_clientes

urlpatterns = [
    path('clientes/', listar_clientes, name='listar_clientes'),
]