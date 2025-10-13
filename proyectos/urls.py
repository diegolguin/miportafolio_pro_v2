from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views
from .views import ProductoViewSet

# Router para la API REST
router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)  # 👈 Prefijo limpio

urlpatterns = [
    # Páginas principales
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista, name='lista'),

    # Registro y autenticación
    path('registro/', views.registrar_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='proyectos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Productos
    path('productos/', views.productos, name='productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:id>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/<int:id>/', views.detalle_producto, name='detalle_producto'),  # 👈 al final siempre
    path('registro/', views.registrar_usuario, name='registrar_usuario'),
    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    # Carrito
    path('carrito/', views.carrito, name='carrito'),
    path('carrito/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('carrito/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),

    # API REST
    path('api/', include(router.urls)),  # 👈 más ordenado, evita conflictos
]

