from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True,upload_to='usuario', default='usuario/user-default.png')

    def get_absolute_url(self):
        return reverse('index')


class Contacto(AbstractUser):
    texto = models.EmailField(null=False, blank=False)
    #null=True, blank=True, upload_to='contacto'

    def get_absolute_url(self):
        return reverse('contacto')

class Post(AbstractUser):
    texto = models.TextField(null=False, blank=False)
    #null=False, upload_to='post'

    def get_absolute_url(self):
        return reverse('post')

class PostGoup(AbstractUser):
    texto = models.TextField()
#null=False