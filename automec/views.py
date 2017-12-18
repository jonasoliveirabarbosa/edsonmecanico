# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect,  render_to_response,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import*
from .models import *
from django.template.context import RequestContext
from django.db.models import Q, Sum, F
from django.contrib.sessions.models import Session
import datetime
import decimal

def site(request):
    return render_to_response('site/theme/index.html')

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('automec.views.resultadoCliente')
    return render_to_response('automec/login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def addUsuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data
            user = User.objects.create_user(valor['nome'], valor['email'],valor['senha'] )
            user.save()
            return redirect('automec.views.addUsuario')
    else:
        form = UsuarioForm()
    return render(request, 'automec/addUsuario.html', {'form': form})

@login_required(login_url='/login/')
def addCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('automec.views.addCliente')
    else:
        form = ClienteForm()
    return render(request, 'automec/addCliente.html', {'form': form})

@login_required(login_url='/login/')
def editCliente(request, cliente_id=None):
    cliente = Cliente.objects.get(pk=cliente_id)
    form = ClienteForm(request.POST, instance=cliente)
    carros =Carro.objects.filter(dono=cliente)
    servicos = Servico.objects.filter(carro__dono=cliente)
    if request.POST:
        if form.is_valid():
            form.save()
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('automec.views.resultadoCliente')
    form = ClienteForm(instance=cliente)
    return render(request, 'automec/addCliente.html', {'form': form,
        'carros':carros, 'servicos':servicos})

@login_required(login_url='/login/')
def verCliente(request, cliente_id=None):
    cliente = Cliente.objects.get(pk=cliente_id)
    carros =Carro.objects.filter(dono=cliente)

    servicos = Servico.objects.filter(carro__dono=cliente)
    return render(request, 'automec/verCliente.html', {'carros':carros,
        'servicos':servicos, 'cliente':cliente})
@login_required(login_url='/login/')
def resultadoCliente(request):
    qs = Cliente.objects.all().order_by('-id')
    return render(request, 'automec/buscaCliente.html', {'qs': qs})

@login_required(login_url='/login/')
def buscarCliente(request):
    q = request.GET.get('q')
    qs2 = Cliente.objects.filter(Q(nome__contains=q) | Q(carro__modelo__contains=q) |
        Q(carro__marca__contains=q) | Q(carro__placa__contains=q)).order_by('-id')[:20]
    return render(request, 'automec/buscaCliente.html', {'qs': qs2})

@login_required(login_url='/login/')
def removeCliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        cliente.delete()
        return redirect('automec.views.resultadoCliente')
    except Servico.DoesNotExist:
        return redirect('automec.views.resultadoCliente')
    return redirect('automec.views.resultadoCliente')

@login_required(login_url='/login/')
def addCarro(request):
    if request.method == "POST":
        form = CarroForm(request.POST)
        if form.is_valid():
            carro = form.save(commit=False)
            carro.save()
            return redirect('automec.views.addCarro')
    else:
        form = CarroForm()

    return render(request, 'automec/addCarro.html', {'form': form})

@login_required(login_url='/login/')
def addServico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.save()

	    servicoD = {}
            servicoD['id'] = servico.id
            servicoD['carro'] = servico.carro.marca+' - '+servico.carro.modelo
            servicoD['valorMaoObra'] = float(servico.valorMaoObra)

            request.session['serv_atual']= servicoD	
            #request.session['serv_atual'] = servico.id
            return redirect('automec.views.servicoSucesso')
    else:
        form = ServicoForm()
    return render(request, 'automec/addServico.html', {'form': form})

@login_required(login_url='/login/')
def editServico(request, servico_id=None):
    servico = Servico.objects.get(pk=servico_id)
    form = ServicoForm(request.POST, instance=servico)
    if request.POST:
        if form.is_valid():
            form.save()
            servico = form.save(commit=False)
            servico.save()
           
	    servicoD = {}
            servicoD['id'] = servico.id
            servicoD['carro'] = servico.carro.marca+' - '+servico.carro.modelo
            servicoD['valorMaoObra'] = float(servico.valorMaoObra)

            return redirect('automec.views.servicoSucesso')
    form = ServicoForm(instance=servico)
    return render(request, 'automec/addServico.html', {'form': form})

@login_required(login_url='/login/')
def ativarServico(request,servico_id):
    try:
        servico = Servico.objects.get(pk=servico_id)
	servicoD = {}
        servicoD['id'] = servico.id
        servicoD['carro'] = servico.carro.marca+' - '+servico.carro.modelo
        servicoD['valorMaoObra'] = float(servico.valorMaoObra)

	
        request.session['serv_atual'] = servicoD
        return redirect('automec.views.resultadoServico')
    except Peca.DoesNotExist:
        return redirect('automec.views.resultadoServico')
    return redirect('automec.views.resultadoServico')

@login_required(login_url='/login/')
def removeServico(request, servico_id):
    try:
        servico = Servico.objects.get(pk=servico_id)
        servico.delete()

    except Servico.DoesNotExist:
        return redirect('automec.views.resultadoServico')
    if 'serv_atual' in request.session:
        del request.session['serv_atual']
    return redirect('automec.views.resultadoServico')

@login_required(login_url='/login/')
def servicoSucesso(request):
    servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
    carro = servico.carro
    return render(request, 'automec/servicoSucesso.html',{"servico":servico})

@login_required(login_url='/login/')
def SemAtivar(request):
    return render(request, 'automec/semAtivado.html')

@login_required(login_url='/login/')
def addPeca(request):
    try:
        servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
    except (Session.DoesNotExist, KeyError):
        return redirect('automec.views.SemAtivar')

    if request.method == "POST":
        form = PecaForm(request.POST)
        if form.is_valid():
            peca = form.save(commit=False)
	    servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
            peca.servico = servico
            peca.save()
            return redirect('automec.views.addPeca')
    else:
        form = PecaForm()

    pecas = Peca.objects.filter(servico=request.session['serv_atual']['id'])
    return render(request, 'automec/addPeca.html', {'form': form, 'pecas':pecas,
        'valorTotalPecas':calcularValorPecas(request),
        'valorTotal':calcularValorTotal(request)})

@login_required(login_url='/login/')
def addPagamento(request):
    try:
        servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
    except (Session.DoesNotExist, KeyError):
        return redirect('automec.views.SemAtivar')

    if request.method == "POST":
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
	    servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
            pagamento.servico = servico
            pagamento.save()
            return redirect('automec.views.addPagamento')
    else:
        form = PagamentoForm()

    pagamentos = Pagamento.objects.filter(servico=request.session['serv_atual']['id'])
    return render(request, 'automec/addPagamento.html', {'form': form, 'pagamentos':pagamentos,
        'valorTotal':calcularValorTotal(request), 'pago':calcularValorPago(request),
        'pagar':(calcularValorTotal(request) - calcularValorPago(request))})

@login_required(login_url='/login/')
def removePeca(request, peca_id):
    form = PecaForm()
    if 'serv_atual' in request.session:
	servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
        pecas = Peca.objects.filter(servico=servico)

    try:
        peca = Peca.objects.get(pk=peca_id)
        peca.delete()
        return redirect('automec.views.addPeca')
    except Peca.DoesNotExist:
        return redirect('automec.views.addPeca')
    return redirect('automec.views.addPeca')

@login_required(login_url='/login/')
def editPeca(request, peca_id=None):
    peca = Peca.objects.get(pk=peca_id)
    form = PecaForm(request.POST, instance=peca)
    if request.POST:
        if form.is_valid():
            form.save()
            peca = form.save(commit=False)
            peca.save()
            return redirect('automec.views.addPeca')
    else:
        form = PecaForm(instance=peca)

    servico = Servico.objects.get(pk=request.session['serv_atual']['id'])	
    pecas = Peca.objects.filter(servico=servico)
    return render(request, 'automec/addPeca.html', {'form': form, 'pecas':pecas,
        'valorTotalPecas':calcularValorPecas(request),
        'valorTota':calcularValorTotal(request)})

@login_required(login_url='/login/')
def editPagamento(request,pagamento_id):
    pagamento = Pagamento.objects.get(pk=pagamento_id)
    if request.method == "POST":
        form = PagamentoForm(request.POST,instance=pagamento)

        if form.is_valid():
            pagamento = form.save(commit=False)
            servico = Servico.objects.get(pk=request.session['serv_atual']['id']) 	
            pagamento.servico = servico
            pagamento.save()
            return redirect('automec.views.addPagamento')
    else:
        form = PagamentoForm(instance = pagamento)

    servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
    pecas = Peca.objects.filter(servico=servico)
    pagamentos = Pagamento.objects.filter(servico=servico)
    return render(request, 'automec/addPagamento.html', {'form': form, 'pagamentos':pagamentos,
        'valorTotal':calcularValorTotal(request), 'pago':calcularValorPago(request),
        'pagar':(calcularValorTotal(request) - calcularValorPago(request))})

@login_required(login_url='/login/')
def removePagamento(request, pagamento_id):
    form = PagamentoForm()

    servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
    pagamentos = Pagamento.objects.filter(servico=servico)

    try:
        pagamento = Pagamento.objects.get(pk=pagamento_id)
        pagamento.delete()
        return redirect('automec.views.addPagamento')
    except Peca.DoesNotExist:
        return redirect('automec.views.addPagamento')
    return redirect('automec.views.addPagamento')

@login_required(login_url='/login/')
def buscarServico(request):
    q = request.GET.get('q')
    qs = Servico.objects.filter(Q(carro__marca__istartswith=q) |
        Q(carro__modelo__istartswith=q) | Q(carro__dono__nome__istartswith=q) | Q(carro__placa__istartswith=q)).order_by('data')

    return render(request, 'automec/buscaServico.html', {'qs': qs})

@login_required(login_url='/login/')
def resultadoServico(request):
    qs = Servico.objects.all().order_by('data')[:20]
    return render(request, 'automec/buscaServico.html', {'qs': qs})

@login_required(login_url='/login/')
def imprimir(request):
    try:
	servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
        total = servico.valorMaoObra + calcularValorPecas(request)
    except (Session.DoesNotExist, KeyError):
        return redirect('automec.views.SemAtivar')
    carro = servico.carro
    cliente = carro.dono
    pecas = Peca.objects.filter(servico=servico)
    pagamentos = Pagamento.objects.filter(servico=servico)

    return render(request, 'automec/imprimir.html',{'cliente':cliente,'carro':carro,
        'pecas':pecas,'valorPecas':calcularValorPecas(request),'pagamentos':pagamentos,'valorTotal':calcularValorTotal(request),
        'pago':calcularValorPago(request),'pagar':(calcularValorTotal(request) - calcularValorPago(request))})

@login_required(login_url='/login/')
def rendimentos(request):
    now = datetime.datetime.now()
    if request.GET.get('q') is not None:
        q = request.GET.get('q')
        q = int(q)
        mesAtual = q
        servicos = Servico.objects.filter(data__year= now.year ,data__month=q)
    else:
        mesAtual = now.month
        servicos = Servico.objects.filter(data__year= now.year ,data__month=now.month)



    return render(request, 'automec/rendimentos.html',{'servicos':servicos,'mesAtual':mesAtual,
        'somaTotal':calcularTotalServicos(servicos), 'totalPago': calcularTotalPago(servicos),
        'totalPagar':calcularTotalApagar(servicos)})

@login_required(login_url='/login/')
def gastos(request):
    now = datetime.datetime.now()
    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.save()
            return redirect('automec.views.gastos')
    else:
        form = GastoForm()

    gastos = Gasto.objects.filter()
    return render(request, 'automec/gastos.html', {'form': form, 'gastos':gastos,
        'valorTotalgastos':100, })

def calcularValorPecas(request):
    valorPecas = decimal.Decimal('0.00')
    try:
	servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
        pecas = Peca.objects.filter(servico=servico)
        for peca in pecas:
            valorPecas = valorPecas + peca.valor
        return valorPecas
    except (Session.DoesNotExist, KeyError):
        return 0

def calcularValorPago(request):
    totalPagamentos = decimal.Decimal('0.00')
    try:
        pagamento = Pagamento.objects.filter(servico=request.session['serv_atual']['id'])
        for pagamento in pagamento:
            totalPagamentos = pagamento.valor + totalPagamentos
        return totalPagamentos
    except (Session.DoesNotExist, KeyError):
        return 0

def calcularValorTotal(request):
    total = decimal.Decimal('0.00')
    try:
	servico = Servico.objects.get(pk=request.session['serv_atual']['id'])
        total = servico.valorMaoObra + calcularValorPecas(request)
        return total
    except (Session.DoesNotExist, KeyError):
        return 0

def calcularTotalServicos(servicos):
    total = decimal.Decimal('0.00')
    for servico in servicos:
        total = servico.valorTotal() + total

    return total

def calcularTotalApagar(servicos):
    total = decimal.Decimal('0.00')
    for servico in servicos:
            total = servico.valorApagar() + total

    return total

def calcularTotalPago(servicos):
    total = decimal.Decimal('0.00')
    for servico in servicos:
            total = servico.valorPago() + total
    return total

class ClienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Cliente.objects.all()

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)
        return qs

class CarroClienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Carro.objects.all()

        if self.q:
            qs = qs.filter(Q(dono__nome__istartswith=self.q) |
                Q(modelo__istartswith=self.q) | Q(marca__istartswith=self.q))
        return qs
