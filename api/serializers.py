from rest_framework import serializers
from .models import Rifa, Bilhete

class RifaSerializer(serializers.ModelSerializer):
    bilhetes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Rifa
        fields = ['id', 'nome', 'descricao', 'data_sorteio', 'bilhetes']

class BilheteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilhete
        fields = '__all__'