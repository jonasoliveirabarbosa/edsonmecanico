from django.urls import path
from . import views
from automec.views import ClienteAutocomplete, CarroClienteAutocomplete

urlpatterns = [

    #paths Sistema
    path('', views.site, name='site'),
    path('usuario/novo/', views.addUsuario, name='add_usuario'),
    path('servico/imprimir/', views.imprimir, name='imprimir'),
    path('login/', views.login_user, name='login'),

    #paths Cliente
    path('cliente/novo/', views.addCliente, name='add_cliente'),
    path('cliente/<int:cliente_id>/remove/', views.removeCliente, name='remover_servico'),
    path('cliente/<int:cliente_id>/ver/', views.verCliente, name='ver_cliente'),
    path('cliente/<int:cliente_id>/editar/', views.editCliente, name= 'editar_servico'),
    path('cliente/resultados/', views.resultadoCliente, name='resultado_cliente'),
    path('cliente/busca/', views.buscarCliente, name='buscar_cliente'),

    #paths carro
    path('carro/novo/', views.addCarro, name='add_carro'),

    #paths servico
    path('servico/novo/', views.addServico, name='add_servico'),
    path('servico/sucesso/', views.servicoSucesso, name='sucesso'),
    path('servico/semAtivar/', views.SemAtivar, name='sem_ativar'),
    path('servico/resultados/', views.resultadoServico, name='resultado_servico'),
    path('servico/busca/', views.buscarServico, name='buscar_servico'),
    path('servico/<int:servico_id>/remove/', views.removeServico, name='remover_servico'),
    path('servico/<int:servico_id>/ativar/', views.ativarServico, name='ativar_servico'),
    path('servico/<int:servico_id>/editar/', views.editServico, name= 'editar_servico'),

    #paths peca
    path('peca/<int:peca_id>/remove/', views.removePeca, name='remover_peca'),
    path('peca/<int:peca_id>/editar/', views.editPeca, name= 'editar_peca'),
    path('peca/novo/', views.addPeca, name='add_peca'),

    #paths pagamento
    path('pagamento/novo/', views.addPagamento, name='add_pagamento'),
    path('pagamento/<int:pagamento_id>/remove/', views.removePagamento, name='remover_pagamento'),
    path('pagamento/<int:pagamento_id>/editar/', views.editPagamento, name= 'editar_pagamento'),

    #paths cliente
    path('cliente-autocomplete/',ClienteAutocomplete.as_view(),name='cliente-autocomplete'),
    path('clientecarro-autocomplete/',CarroClienteAutocomplete.as_view(),name='clientecarro-autocomplete'),
    path('rendimento/', views.rendimentos, name='rendimento'),

    #paths gasto
    path('gasto/', views.gastos, name='ver_gastos'),
    #path(r'^gasto/(<gasto_id>)/remove/$', views.removeGasto, name='remover_gasto'),
    #path(r'^gasto/(<gasto_id>)/editar/$', views.editGasto, name= 'editar_gasto'),
    #path(r'^gasto/novo/$', views.addCusto, name='add_gasto'),

    #paths custo
    #path(r'^custo/(<custo_id>)/remove/$', views.removeCusto, name='remover_custo'),
    #path(r'^custo/(<custo_id>)/editar/$', views.editCusto, name= 'editar_custo'),
    #path(r'^custo/novo/$', views.addCusto, name='add_custo'),

]
