from rest_framework import serializers
from .models import Producto, Categoria, Marca, Movimiento

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.ReadOnlyField(source='marca.nombre')
    nombre_categoria = serializers.ReadOnlyField(source='categoria.nombre')
    
    class Meta:
        model = Producto
        fields = [
            'id', 'sku', 'nombre', 'descripcion', 
            'marca', 'nombre_marca',
            'categoria', 'nombre_categoria',
            'peso_kg', 'stock_actual', 'volumen_m3',
            'largo_cm', 'ancho_cm', 'alto_cm' 
        ]


class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'