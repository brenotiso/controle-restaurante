from rest_framework import routers
from .viewsets import (
    AdicionalViewSet,
    CategoriaViewSet,
    ProdutoViewSet,
    MesaViewSet,
    PedidoDetalheViewSet,
    PedidoViewSet
)


router = routers.DefaultRouter(trailing_slash=False)
router.register('adicionais', AdicionalViewSet)
router.register('categorias', CategoriaViewSet)
router.register('produtos', ProdutoViewSet)
router.register('mesas', MesaViewSet)
router.register('pedidos_detalhe', PedidoDetalheViewSet)
router.register('pedidos', PedidoViewSet)

urlpatterns = router.urls
