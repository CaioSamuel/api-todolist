from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=155)
    descricao = models.TextField(max_length=300)
    concluida = models.BooleanField(default=False)
    data_de_criacao = models.DateTimeField(auto_now_add=True)