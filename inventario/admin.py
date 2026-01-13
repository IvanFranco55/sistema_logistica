from django.contrib import admin
from .models import Producto, Marca, Categoria, Movimiento

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'marca', 'categoria', 'mostrar_volumen', 'stock_actual')
    
    # Buscador por nombre o código
    search_fields = ('nombre', 'sku')
    
    # Filtros laterales
    list_filter = ('es_fragil', 'created_at')
    def mostrar_volumen(self, obj):
        return f"{obj.volumen_m3} m³"
    mostrar_volumen.short_description = "Volumen Real"

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'producto', 'tipo', 'cantidad', 'observacion')
    list_filter = ('tipo', 'fecha')
    search_fields = ('producto__nombre',) 