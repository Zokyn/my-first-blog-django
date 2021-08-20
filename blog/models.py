from datetime import time
from django.conf import settings
from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    texto = models.TextField
    titulo = models.CharField(max_length=200)
    data_criado = models.DateTimeField(default=timezone.now)
    data_publicado = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo