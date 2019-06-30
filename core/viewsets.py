from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    status,
    viewsets
)
from rest_framework.response import Response
from .models import (
    Adicional,
    Categoria,
    Produto,
    Mesa,
    Pedido_Detalhe,
    Pedido
)
from .serializers import (
    AdicionalSerializer,
    CategoriaSerializer,
    ProdutoSerializer,
    MesaSerializer,
    PedidoDetalheSerializer,
    PedidoSerializer,
    PedidoEdicaoSerializer
)


class AdicionalViewSet(viewsets.ModelViewSet):
    serializer_class = AdicionalSerializer
    queryset = Adicional.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()


class MesaViewSet(viewsets.ModelViewSet):
    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()


class PedidoDetalheViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoDetalheSerializer
    queryset = Pedido_Detalhe.objects.all()

    def create(self, request):
        serializer = PedidoDetalheSerializer(data=request.data)
        if serializer.is_valid():
            produto = Produto.objects.get(pk=request.data['produto'])
            if produto.ativo:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "error": "produto",
                    "error_description": "Produto inativo."
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('visto', 'baixa', 'mesa')

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            serializer_class = PedidoEdicaoSerializer

        return serializer_class
