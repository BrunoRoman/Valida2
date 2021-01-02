from rest_framework.viewsets import ModelViewSet
from network.models import *
from .serializers import InternetSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.decorators import action

from internet.valida.classes import Router
from network.network_templates.controller import save
import json

class InternetViewSet(ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = InternetSerializer

    def create(self, request, *args, **kwargs):
        try:
            router = Router(request.data['hostname'],request.data['ip'],request.data['netmiko'],json.loads(request.data['comandos']))
            router.ospf_int = router.ospf_int 
            router.ospf_neighbor = router.ospf_neighbor
            if save(router,request):
                return Response(status=status.HTTP_201_CREATED,data={'Result':'criado com sucesso'})
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})
        except Exception as ident:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Result':ident})
