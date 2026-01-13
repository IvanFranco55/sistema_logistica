from rest_framework import viewsets, filters
from django.db.models import Sum, F, Value, Q
from django.db.models.functions import Coalesce
from .models import Producto, Categoria, Marca, Movimiento
from .serializers import ProductoSerializer, CategoriaSerializer, MarcaSerializer, MovimientoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # --- AGREGA ESTA LÍNEA (Es el "Carnet de Identidad" para el Router) ---
    queryset = Producto.objects.all() 
    # -----------------------------------------------------------------------
    
    serializer_class = ProductoSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'sku', 'marca__nombre', 'categoria__nombre']
    
    ordering_fields = ['peso_kg', 'stock_actual', 'nombre']
    ordering = ['nombre']

    def get_queryset(self):
        # Esta función SOBREESCRIBE a la línea de arriba cuando se ejecuta la consulta real
        return Producto.objects.annotate(
            total_entradas=Coalesce(Sum('movimientos__cantidad', filter=Q(movimientos__tipo='ENTRADA')), 0),
            total_salidas=Coalesce(Sum('movimientos__cantidad', filter=Q(movimientos__tipo='SALIDA')), 0)
        ).annotate(
            stock_actual=F('total_entradas') - F('total_salidas')
        )

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['producto__nombre', 'tipo']
    ordering_fields = ['fecha', 'cantidad']