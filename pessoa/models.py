from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100)
    ativado = models.BooleanField(default=True)
    data_nascimento = models.DateField(null=True)
    #cor = models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self) -> str:
        return super().__str__() #return self.nome_completo