from rest_framework import serializers
from .models import Producto, Cliente

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
from .cart import Cart
from .models import Producto
from rest_framework import serializers

class CarritoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    precio = serializers.DecimalField(max_digits=10, decimal_places=2)
    cantidad = serializers.IntegerField()
    subtotal = serializers.SerializerMethodField()

    def get_subtotal(self, obj):
        return obj['precio'] * obj['cantidad']
