from rest_framework.viewsets import ModelViewSet
from network.models import *
from .serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.decorators import action

from network.tasks import connect_device_task

import requests
import json

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

    @action(detail=True,methods=['put'])
    def atualizar(self,request,pk=None):
        try:
            m = Modelo.objects.get(id=pk)
            m.comandos.set(request.data['comandos'])
            print(pk)
            return Response(status=status.HTTP_200_OK,data={'Atualizado':m.descricao})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})

class ComandoViewSet(ModelViewSet):
    queryset = Comando.objects.all()
    serializer_class = ComandoSerializer

    
class EquipamentoViewSet(ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

    def create(self, request, *args, **kwargs):
        try:
            Equipamento.objects.create(hostname=request.data['hostname'],ip=request.data['ip'],modelo=Modelo.objects.get(id=int(request.data['modelo'])))
            return Response(status=status.HTTP_201_CREATED,data={'Result':'criado com sucesso'})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})

class AmbienteViewSet(ModelViewSet):
    
    serializer_class = AmbienteSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id',None)
        nome = self.request.query_params.get('nome',None)
        queryset = Ambiente.objects.all()
        if id:
            queryset = Ambiente.objects.filter(id=id)
        elif nome:
            queryset = Ambiente.objects.filter(nome=nome)
        else:
            queryset = Ambiente.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            a = Ambiente(nome=request.data['nome'])
            a.save()
            for equip in request.data['equipamentos']:
                a.equipamentos.add(Equipamento.objects.get(id=equip))
            return Response(status=status.HTTP_201_CREATED,data={'Result':'criado com sucesso'})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':str(ident)})
    
    @action(detail=True,methods=['put'])
    def atualizar(self,request,pk=None):
        try:
            a = Ambiente.objects.get(id=pk)
            a.equipamentos.set(request.data['equipamentos'])
            return Response(status=status.HTTP_200_OK,data={'atualizado':a.nome})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':str(ident)})


    @action(detail=True,methods=['post'])
    def validar(self,request,pk=None):
        try: 
            a = Ambiente.objects.get(id=pk)
            print(a.nome)
            equipamentos = a.equipamentos.all().values()
            for i in range(len(equipamentos)):
                equipamentos[i]['ambiente'] = a.nome
                modelos = Modelo.objects.get(id=equipamentos[i]['modelo_id'])
                comandos = modelos.comandos.all().values()
                equipamentos[i]['netmiko'] = modelos.netmiko
                dict_comandos = {}
                for j in range(len(comandos)):
                    dict_comandos[comandos[j]['nome']] = comandos[j]['sintaxe']
                equipamentos[i]['comandos'] = json.dumps(dict_comandos)
            for equip in equipamentos:
                result = connect_device_task.delay(a.nome,equipamentos[i])
                #response = requests.post('http://127.0.0.1:8000/internet/',data=equipamentos[1],auth=('admin','admin'))
            return Response(status=status.HTTP_201_CREATED,data={'ok':'criado'})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':str(ident)})


      
    