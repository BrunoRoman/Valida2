from rest_framework import serializers
from network.models import *



class ComandoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comando
        fields = ('id','nome','sintaxe')

class ModeloSerializer(serializers.ModelSerializer):

    comandos = ComandoSerializer(many=True)

    class Meta:
        model = Modelo
        fields = ("id",'nome','descricao','netmiko','comandos')

class EquipamentoSerializer(serializers.ModelSerializer):
    modelo = ModeloSerializer()
    class Meta:
        model = Equipamento
        fields = ('id','hostname','ip','modelo')
    
class AmbienteSerializer(serializers.ModelSerializer):
     
     equipamentos = EquipamentoSerializer(many=True)
     
     class Meta:
        model = Ambiente
        fields = ('id','nome','equipamentos')
     
        