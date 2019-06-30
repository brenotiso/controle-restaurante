from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Adicional(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.CharField('Descrição', max_length=300, blank=True, null=True)
    adicionais = models.ManyToManyField(Adicional, related_name='categorias')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.CharField('Descrição', max_length=300)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    ativo = models.BooleanField(default=True)
    categoria = models.OneToOneField(Categoria, related_name='produtos', on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Mesa(models.Model):
    disponivel = models.BooleanField('Disponível', null=True, default=True)

    def __str__(self):
        return str(self.id)


class Pedido_Detalhe(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    observacao = models.CharField('Observação', max_length=400)
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.produto.__str__()


class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, related_name='pedidos', on_delete=models.PROTECT)
    pedido_detalhe = models.ManyToManyField(Pedido_Detalhe, related_name='pedidos')
    baixa = models.BooleanField(default=False)  # quando fechar a mesa é passado para True
    visto = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
