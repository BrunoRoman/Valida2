from django.db import models

class Comando(models.Model):
    sintaxe = models.CharField(max_length=100)
    

    class Meta:
        ordering = ['sintaxe']

    def __str__(self):
        return self.sintaxe


class Modelo(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    netmiko = models.CharField(max_length=20)
    comandos = models.ManyToManyField(Comando)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao

class Equipamento(models.Model):
    hostname = models.CharField(max_length=100)
    ip = models.CharField(max_length=15)
    modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE,related_name='equipamentos')

    class Meta:
        ordering = ['hostname']

    def __str__(self):
        return self.hostname

class Ambiente(models.Model):
    nome = models.CharField(max_length=50)
    equipamentos = models.ManyToManyField(Equipamento)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

