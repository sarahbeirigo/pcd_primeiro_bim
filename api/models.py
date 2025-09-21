from django.db import models

class Rifa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_sorteio = models.DateTimeField()

    def __str__(self):
        return self.nome

class Bilhete(models.Model):
    rifa = models.ForeignKey(Rifa, on_delete=models.CASCADE, related_name='bilhetes')
    numero = models.IntegerField()
    comprador = models.CharField(max_length=100)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return f'Bilhete {self.numero} da rifa {self.rifa.nome}'