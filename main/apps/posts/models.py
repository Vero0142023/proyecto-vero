from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Comentario(models.Model):
    posts = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


class Categoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.titulo   




class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True,default='Sin categoría')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)

    def _str_(self):
        return self.titulo

    def delete(self,using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

class Contacto(models.Model):
    nombre = models.CharField(max_length = 50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    website = models.CharField(max_length = 50)
    asunto = models.CharField(max_length = 100)
    mensaje = models.TextField()


def __str__(self):
    return self.nombre

def __str__(self):
    return self.texto

#Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def _str_(self):
        return self.nombre

