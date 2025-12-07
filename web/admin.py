from django.contrib import admin
from .models import Torta, Categoria, Testimonio

# Configuramos para que el "slug" se llene solo automáticamente al escribir el nombre
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Torta)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Testimonio)