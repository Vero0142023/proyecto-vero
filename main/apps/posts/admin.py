from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'resumen', 'contenido', 'fecha_publicacion',
                    'activo', 'categoria', 'image', 'publicado', 'editor')

admin.site.register(Categoria)