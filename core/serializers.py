from rest_framework import serializers
from .models import (
    Adicional,
    Categoria,
    Produto,
    Mesa,
    Pedido_Detalhe,
    Pedido
)


class AdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adicional
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'


class PedidoDetalheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Detalhe
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ('baixa',)
