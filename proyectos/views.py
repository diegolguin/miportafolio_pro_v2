from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse
from .models import Cliente, Producto
from .forms import RegistroUsuarioForm, ClienteForm, ProductoForm
from .cart import Cart

# Página de inicio
def inicio(request):
    return render(request, 'proyectos/inicio.html')


# Registro de usuarios
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


# Lista principal de módulos
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
    qs = Producto.objects.all().order_by('nombre')
    return render(request, 'proyectos/productos.html', {'productos': qs})


@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'proyectos/editar_producto.html', {'form': form})


@login_required
def editar_producto(request, id):
    obj = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=obj)
    return render(request, 'proyectos/editar_producto.html', {'form': form})


@login_required
def eliminar_producto(request, id):
    obj = get_object_or_404(Producto, pk=id)
    obj.delete()
    return redirect('productos')


# ================================
# 👥 Clientes
# ================================

@login_required
def lista_clientes(request):
    qs = Cliente.objects.all().order_by('-creado')
    return render(request, 'proyectos/clientes.html', {'clientes': qs})


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
    obj = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=obj)
    return render(request, 'proyectos/editar_cliente.html', {'form': form})


@login_required
def eliminar_cliente(request, id):
    obj = get_object_or_404(Cliente, pk=id)
    obj.delete()
    return redirect('lista_clientes')


# ================================
# 🛒 Carrito
# ================================

# Carrito
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .cart import Cart

@login_required
def add_to_cart(request, id):
    producto = get_object_or_404(Producto, pk=id)
    cart = Cart(request)
    cart.add(producto.id, producto.nombre, producto.precio, qty=1)
    return redirect('carrito')

@login_required
def carrito(request):
    cart = Cart(request)
    cart_items = []

    for item in cart.items():
        cart_items.append({
            'id': item['id'],
            'nombre': item['name'],  # corregido
            'precio': item['price'], # corregido
            'cantidad': item['qty'],
            'subtotal': item['subtotal']
        })

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
