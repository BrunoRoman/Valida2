from rest_framework import serializers
from network.models import Resultado

class InternetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ('id','data','ambiente','hostname','comando','output')