from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

base_url = 'http://www.guiadosquadrinhos.com/'

element_pesquisar = 'TextBusca'

element_selecionar = 'stateList'

element_botao = 'busca'

value_selecionar = 'edi'

get_nome_editora = '//*[@id="editora"]'

@given(u'acesso a página inicial do Guia dos Quadrinhos')
def step_impl(context):
	context.web.get(base_url)
    # raise NotImplementedError(u'STEP: Given acesso a página inicial do Guia dos Quadrinhos')


@when(u'clico no input de Pesquisar por')
def step_impl(context):
	context.web.implicitly_wait(25)

	context.element_pesquisar = context.web.find_element_by_id(element_pesquisar)

	context.element_pesquisar.click()
    # raise NotImplementedError(u'STEP: When clico no input de Pesquisar por')


@when(u'digito Pipoca no input')
def step_impl(context):
	context.element_pesquisar.send_keys('Pipoca')
    # raise NotImplementedError(u'STEP: When digito Pipoca no input')


@when(u'escolho no select a opção Editora')
def step_impl(context):
	context.element_selecionar = Select(context.web.find_element_by_id(element_selecionar))

	context.element_selecionar.select_by_value(value_selecionar)
    # raise NotImplementedError(u'STEP: When escolho no select a opção Editora')


@when(u'clico em Pesquisar')
def step_impl(context):
	context.element_botao = context.web.find_element_by_id(element_botao)

	context.element_botao.click()
    # raise NotImplementedError(u'STEP: When clico em Pesquisar')


@then(u'devo ver a página da Editora')
def step_impl(context):
	context.web.implicitly_wait(25)

	context.get_nome_editora = context.web.find_element_by_xpath(get_nome_editora)

	nome_editora = context.get_nome_editora.text

	print(nome_editora)
    #raise NotImplementedError(u'STEP: Then devo ver a página da Editora')


@when(u'digito Panini no input')
def step_impl(context):
	context.element_pesquisar.send_keys('Panini')
    # raise NotImplementedError(u'STEP: When digito Panini no input')
