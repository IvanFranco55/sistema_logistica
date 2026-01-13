from django.db import models
from django.db.models import Sum

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorías"

class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # Relaciones (Foreign Keys)
    # on_delete=models.PROTECT evita que si borras la marca "Samsung", se borren los monitores.
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos', null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='productos', null=True, blank=True)

    # Identificación
    sku = models.CharField(max_length=50, unique=True, help_text="Código único (Barras/QR)")
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)

    # Datos Logísticos
    peso_kg = models.DecimalField(max_digits=10, decimal_places=3)
    es_fragil = models.BooleanField(default=False)
    
    # Dimensiones
    largo_cm = models.DecimalField(max_digits=10, decimal_places=2)
    ancho_cm = models.DecimalField(max_digits=10, decimal_places=2)
    alto_cm = models.DecimalField(max_digits=10, decimal_places=2)

    # Auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.nombre}"

    @property
    def volumen_m3(self):
        return (self.largo_cm * self.ancho_cm * self.alto_cm) / 1000000
    
    @property
    def stock_actual(self):
        if hasattr(self, '_stock_cache'):
            return self._stock_cache
            
        entradas = self.movimientos.filter(tipo='ENTRADA').aggregate(total=Sum('cantidad'))['total'] or 0
        salidas = self.movimientos.filter(tipo='SALIDA').aggregate(total=Sum('cantidad'))['total'] or 0
        return entradas - salidas

    @stock_actual.setter
    def stock_actual(self, value):
        self._stock_cache = value
    
class Movimiento(models.Model):
    TIPOS_ACCION = [
        ('ENTRADA', 'Entrada de Stock'),
        ('SALIDA', 'Salida de Stock'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    cantidad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=10, choices=TIPOS_ACCION)
    fecha = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True, null=True, help_text="Ej: Compra a proveedor / Venta #123")

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} ({self.cantidad})"