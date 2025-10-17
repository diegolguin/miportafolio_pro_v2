from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse
from rest_framework import viewsets

from .models import Cliente, Producto
from .serializers import ProductoSerializer, ClienteSerializer
from .forms import RegistroUsuarioForm, ClienteForm, ProductoForm
from .cart import Cart


# ================================
# 🏠 Página de inicio
# ================================
def inicio(request):
    return render(request, 'proyectos/inicio.html')


# ================================
# 👤 Registro de usuarios
# ================================
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'proyectos/registro.html', {'form': form})


# ================================
# 📋 Lista principal de módulos
# ================================
@login_required
def lista(request):
    proyectos = [
        {'nombre': 'Sistema de Ventas', 'url': 'productos'},
        {'nombre': 'Gestión de Clientes', 'url': 'lista_clientes'},
        {'nombre': 'Inventario', 'url': 'productos'},
    ]
    return render(request, 'proyectos/lista.html', {'proyectos': proyectos})


# ================================
# 📦 Productos
# ================================
@login_required
def productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'proyectos/productos.html', {'productos': productos})


@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  # 👈 incluye imágenes
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'proyectos/editar_producto.html', {'form': form})


@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)  # 👈 incluye imágenes
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'proyectos/editar_producto.html', {'form': form})


@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect('productos')


# ✅ NUEVA VISTA: Detalle de producto
@login_required
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'proyectos/detalle_producto.html', {'producto': producto})


# ================================
# 👥 Clientes
# ================================
@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('-creado')
    return render(request, 'proyectos/clientes.html', {'clientes': clientes})


@login_required
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'proyectos/editar_cliente.html', {'form': form})


@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'proyectos/editar_cliente.html', {'form': form})


@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect('lista_clientes')


# ================================
# 🛒 Carrito
# ================================
@login_required
def add_to_cart(request, id):
    producto = get_object_or_404(Producto, pk=id)
    cart = Cart(request)
    cart.add(producto.id, producto.nombre, producto.precio, qty=1)
    return redirect('carrito')


@login_required
def carrito(request):
    cart = Cart(request)
    cart_items = [
        {
            'id': item['id'],
            'nombre': item['name'],
            'precio': item['price'],
            'cantidad': item['qty'],
            'subtotal': item['subtotal']
        }
        for item in cart.items()
    ]
    total = cart.total()
    return render(request, 'proyectos/carrito.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def remove_from_cart(request, id):
    cart = Cart(request)
    cart.remove(id)
    return redirect('carrito')


# ================================
# 🔗 API REST de Productos
# ================================
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def carrito_api(request):
    """Devuelve los productos del carrito en formato JSON"""
    cart = Cart(request)
    data = []

    for item in cart.items():  # 👈 usamos items() porque tu Cart lo maneja así
        data.append({
            'id': item['id'],
            'nombre': item['name'],
            'precio': float(item['price']),
            'cantidad': item['qty'],
            'subtotal': float(item['subtotal'])
        })

    total = float(cart.total())

    return Response({
        'items': data,
        'total': total
    })
