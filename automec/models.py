from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
import re

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    endereco = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    marca = models.CharField(max_length=150)
    modelo = models.CharField(max_length=200)
    placa = models.CharField(max_length=9)
    ano = models.IntegerField(blank = True)
    dono = models.ForeignKey(Cliente)

    def __str__(self):
        return self.marca+' '+self.modelo+' - '+self.dono.nome

class Servico(models.Model):
    valorMaoObra = models.DecimalField(max_digits=8, decimal_places=2)
    carro = models.ForeignKey(Carro)
    data = models.DateField('data',default=timezone.now())
    km = models.IntegerField()

    def valorTotal(self):
        valor = self.valorMaoObra
        pecas = Peca.objects.filter(servico= self)

        for peca in pecas:
            valor = valor + peca.valor

        return valor

    def valorPago(self):
        valor = 0
        pagamentos = Pagamento.objects.filter(servico= self)

        for pagamento in pagamentos:
            valor = valor + pagamento.valor

        return valor

    def valorApagar(self):
        valor = self.valorTotal() - self.valorPago()

        return valor

    def __str__(self):
        return str(self.valorMaoObra)+" "+str(self.km)

class Peca(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    servico = models.ForeignKey(Servico)

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    tipoPagamento = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    parcelas = models.IntegerField()
    data = models.DateField('data', default=timezone.now())
    servico = models.ForeignKey(Servico)

    def __str__(self):
        return self.tipoPagamento

class Custo(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField('data', default=timezone.now())
    descricao = models.CharField(max_length=150)
    servico = models.ForeignKey(Servico)

    def __str__(self):
        return self.descricao

class GastoMensal(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    vencimento = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao


class GastoUnico(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    vencimento = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao


class GastoSemanal(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    diaVencimento = models.DecimalField(max_digits=2, decimal_places=0)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao
