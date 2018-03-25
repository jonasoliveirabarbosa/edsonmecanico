# -*- coding: utf-8 -*-
#!/usr/bin/python
from django import forms
from django.forms.widgets import *
from django.forms import widgets
from .models import *
from dal import autocomplete
from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe
from input_mask.widgets import InputMask

class UsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm , self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class' : 'formulario'})
        self.fields['email'].widget.attrs.update({'class' : 'formulario'})
        self.fields['senha'].widget.attrs.update({'class' : 'formulario'})
    class Meta:
        model = Usuario
        widgets = {'senha': forms.PasswordInput(),}
        fields = ('nome', 'email','senha')


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class' : 'formulario'})
        self.fields['email'].widget.attrs.update({'class' : 'formulario'})
        self.fields['telefone'] = forms.CharField(widget=MascaraTelefone)
        self.fields['telefone'].widget.attrs.update({'id' : 'formulario'})
        self.fields['celular'] = forms.CharField(widget=MascaraCelular)
        self.fields['celular'].widget.attrs.update({'id' : 'formulario'})
        self.fields['endereco'].widget.attrs.update({'class' : 'formulario'})

    class Meta:
        model = Cliente
        fields = ('nome', 'email','telefone','celular','endereco')


class CarroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarroForm, self).__init__(*args, **kwargs)
        self.fields['marca'].widget.attrs.update({'class' : 'formulario'})
        self.fields['modelo'].widget.attrs.update({'class' : 'formulario'})
        self.fields['placa'] = forms.CharField(widget=MascaraPlaca)
        self.fields['placa'].widget.attrs.update({'id' : 'formulario'})
        self.fields['ano'] = forms.IntegerField(widget=MascaraAno)
        self.fields['ano'].widget.attrs.update({'id' : 'formulario'})
    class Meta:
        model = Carro
        fields = ('marca', 'modelo','placa','ano','dono')
        widgets = {
            'dono': autocomplete.ModelSelect2(url='cliente-autocomplete')
        }

class ServicoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServicoForm, self).__init__(*args, **kwargs)
        self.fields['valorMaoObra'].widget.attrs.update({'class' : 'formulario'})
        self.fields['km'].widget.attrs.update({'class' : 'formulario'})
        self.fields['data'].widget.attrs.update({'id' : 'formulario'})

    class Meta:
        model = Servico
        widgets = {'data': forms.DateInput(format='%d/%m/%Y'), }
        fields = ('valorMaoObra', 'carro', 'data','km' )
        widgets = {
            'carro': autocomplete.ModelSelect2(url='clientecarro-autocomplete')
            }

class PecaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PecaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class' : 'formulario'})
        self.fields['valor'].widget.attrs.update({'class' : 'formulario'})
    class Meta:
        model = Peca
        fields = ('nome', 'valor')

class PagamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PagamentoForm, self).__init__(*args, **kwargs)
        PAGAMENTO_CHOICES = (
            ('dinhero','Dinheiro'),
            ('credito', 'Credito'),
            ('debito', 'Débito'),)
        PARCELAS_CHOICES = (('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
            ('7','7'),
            ('8','8'),
            ('9','9'),
            ('10','10'),
            ('11','11'),
            ('12','12'),)
        self.fields['valor'].widget.attrs.update({'class' : 'formulario'})
        self.fields['tipoPagamento'] = forms.ChoiceField(choices= PAGAMENTO_CHOICES, label='Tipo')
        self.fields['tipoPagamento'].widget.attrs.update({'class' : 'choices'})
        self.fields['parcelas'] = forms.ChoiceField(choices= PARCELAS_CHOICES, label='Parcela')
        self.fields['parcelas'].widget.attrs.update({'class' : 'choices'})
        self.fields['data'].widget.attrs.update({'class' : 'formulario'})

    class Meta:
        model = Pagamento
        widgets = {'data': forms.DateInput(format='%d/%m/%Y'),}
        fields = ('tipoPagamento', 'valor','parcelas','data')

class GastoMensalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GastoForm, self).__init__(*args, **kwargs)
        self.fields['vencimento'].widget.attrs.update({'class' : 'formulario'})
        self.fields['valor'].widget.attrs.update({'class' : 'formulario'})
        self.fields['descricao'].widget.attrs.update({'class' : 'formulario'})
    class Meta:
        model = GastoMensal
        widgets = {'vencimento': forms.DateInput(format='%d/%m/%Y'),}
        fields = ('valor', 'vencimento','descricao')


# class GastoForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(GastoForm, self).__init__(*args, **kwargs)
#         PERIODO_CHOICES = (
#             ('unico','Unico'),
#             ('semanal', 'Semanal'),
#             ('mensal', 'Mensal'),)
#         self.fields['valor'].widget.attrs.update({'class' : 'formulario'})
#         self.fields['periodicidade'] = forms.ChoiceField(choices= PERIODO_CHOICES, label='Periodicidade')
#         self.fields['periodicidade'].widget.attrs.update({'class' : 'choices'})
#         self.fields['descricao'].widget.attrs.update({'class' : 'formulario'})
#     class Meta:
#         model = Gasto
#         fields = ('valor', 'periodicidade','descricao')

class MascaraTelefone(InputMask):
    mask = {'mask': '9999-9999'}

class MascaraCelular(InputMask):
    mask = {'mask': '99999-9999'}

class MascaraPlaca(InputMask):
    mask = {'mask': 'ZZZ-9999'}

class MascaraAno(InputMask):
    mask = {'mask': '9999'}
