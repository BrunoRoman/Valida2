from rest_framework.viewsets import ModelViewSet
from network.models import *
from .serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

    def create(self, request, *args, **kwargs):
        try:
            m = Modelo(nome=request.data['nome'],descricao=request.data['descricao'],netmiko=request.data['netmiko'])
            m.save()
            for cmd in request.data['comandos']:
                m.comandos.add(Comando.objects.get(id=cmd))
            return Response(status=status.HTTP_201_CREATED,data={'Result':'criado com sucesso'})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})

class ComandoViewSet(ModelViewSet):
    queryset = Comando.objects.all()
    serializer_class = ComandoSerializer

    
class EquipamentoViewSet(ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    """
    def create(self, validated_data):
        try:
            equipamento = validated_data['equipamentos']
            Equipamento.objects.create(**equipamento)
            equipamento.modelo=Modelo.objects.get(id=int(request.data['modelo']))
            equipamento.save()
            return Response(status=status.HTTP_201_CREATED,data=equipamento)
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})
    """
    def create(self, request, *args, **kwargs):
        try:
            Equipamento.objects.create(hostname=request.data['hostname'],ip=request.data['ip'],modelo=Modelo.objects.get(id=int(request.data['modelo'])))
            return Response(status=status.HTTP_201_CREATED,data={'Result':'criado com sucesso'})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})

class AmbienteViewSet(ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

    def create(self, request, *args, **kwargs):
        try:
            a = Ambiente(nome=request.data['nome'])
            a.save()
            for equip in request.data['equipamentos']:
                a.equipamentos.add(Equipamento.objects.get(id=equip))
            return Response(status=status.HTTP_201_CREATED,data={'Result':'criado com sucesso'})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})
            
    