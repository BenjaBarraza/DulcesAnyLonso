from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Categoría")
    # El slug es una versión del nombre apta para código (ej: "Sin Azúcar" -> "sin-azucar")
    slug = models.SlugField(unique=True, verbose_name="Identificador (Slug)")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


# Tortas    
class Torta(models.Model):
    # Vinculamos la torta a una categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoría")
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Torta")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='tortas/', verbose_name="Foto")
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio (Opcional)")
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Torta"
        verbose_name_plural = "Tortas"


# Testimonios
class Testimonio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    mensaje = models.TextField(verbose_name="Comentario")
    # Puntuación de 1 a 5
    puntuacion = models.IntegerField(default=5, choices=[(i, str(i)) for i in range(1,6)], verbose_name="Estrellas")
    visible = models.BooleanField(default=True, verbose_name="¿Mostrar en la web?")
    
    def __str__(self):
        return f"{self.nombre} ({self.puntuacion}★)"

    # Truco para iterar estrellas en el HTML
    def get_estrellas(self):
        return range(self.puntuacion)
    
    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"