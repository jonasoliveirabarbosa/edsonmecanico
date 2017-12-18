from django.conf.urls import include, url
from . import views
from automec.views import ClienteAutocomplete, CarroClienteAutocomplete

urlpatterns = [

    #Urls Sistema
    url(r'^$', views.site, name='site'),
    url(r'^usuario/novo/$', views.addUsuario, name='add_usuario'),
    url(r'^$', views.addCliente),
    url(r'^servico/imprimir/', views.imprimir, name='imprimir'),
    url(r'^login/$', views.login_user, name='login'),

    #Urls Cliente
    url(r'^cliente/novo/$', views.addCliente, name='add_cliente'),
    url(r'^$', views.addCarro),
    url(r'^cliente/(?P<cliente_id>\d+)/remove/$', views.removeCliente, name='remover_servico'),
    url(r'^cliente/(?P<cliente_id>\d+)/ver/$', views.verCliente, name='ver_cliente'),
    url(r'^cliente/(?P<cliente_id>\d+)/editar/$', views.editCliente, name= 'editar_servico'),
    url(r'^cliente/resultados/$', views.resultadoCliente, name='resultado_cliente'),
    url(r'^cliente/busca/$', views.buscarCliente, name='buscar_cliente'),

    #urls carro
    url(r'^carro/novo/$', views.addCarro, name='add_carro'),

    #urls servico
    url(r'^$', views.addServico),
    url(r'^servico/novo/$', views.addServico, name='add_servico'),
    url(r'^$', views.servicoSucesso),
    url(r'^servico/sucesso/', views.servicoSucesso, name='sucesso'),
    url(r'^servico/semAtivar/', views.SemAtivar, name='semAtivar'),
    url(r'^servico/resultados/$', views.resultadoServico, name='resultado_servico'),
    url(r'^servico/busca/$', views.buscarServico, name='buscar_servico'),
    url(r'^servico/(?P<servico_id>\d+)/remove/$', views.removeServico, name='remover_servico'),
    url(r'^servico/(?P<servico_id>\d+)/ativar/$', views.ativarServico, name='ativar_servico'),
    url(r'^servico/(?P<servico_id>\d+)/editar/$', views.editServico, name= 'editar_servico'),

    #urls peca
    url(r'^peca/$', views.addPeca),
    url(r'^peca/(?P<peca_id>\d+)/remove/$', views.removePeca, name='remover_peca'),
    url(r'^peca/(?P<peca_id>\d+)/editar/$', views.editPeca, name= 'editar_peca'),
    url(r'^peca/novo/$', views.addPeca, name='add_peca'),

    #urls pagamento
    url(r'^$', views.addPagamento),
    url(r'^pagamento/novo/$', views.addPagamento, name='add_pagamento'),
    url(r'^pagamento/(?P<pagamento_id>\d+)/remove/$', views.removePagamento, name='remover_pagamento'),
    url(r'^pagamento/(?P<pagamento_id>\d+)/editar/$', views.editPagamento, name= 'editar_pagamento'),

    #urls cliente
    url(r'^cliente-autocomplete/$',ClienteAutocomplete.as_view(),name='cliente-autocomplete'),
    url(r'^clientecarro-autocomplete/$',CarroClienteAutocomplete.as_view(),name='clientecarro-autocomplete'),
    url(r'^rendimento/$', views.rendimentos, name='rendimento'),

    #urls gasto
    url(r'^gasto/$', views.gastos, name='ver_gastos'),
    #url(r'^gasto/(?P<gasto_id>\d+)/remove/$', views.removeGasto, name='remover_gasto'),
    #url(r'^gasto/(?P<gasto_id>\d+)/editar/$', views.editGasto, name= 'editar_gasto'),
    #url(r'^gasto/novo/$', views.addCusto, name='add_gasto'),

    #urls custo
    #url(r'^custo/(?P<custo_id>\d+)/remove/$', views.removeCusto, name='remover_custo'),
    #url(r'^custo/(?P<custo_id>\d+)/editar/$', views.editCusto, name= 'editar_custo'),
    #url(r'^custo/novo/$', views.addCusto, name='add_custo'),

]
