from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

element_selecionar = 'stateList'

value_selecionar_artista = 'arte'

get_nome_artista = '//*[@id="artista"]'

@when(u'digito Adriana Melo no input')
def step_impl(context):
	context.element_pesquisar.send_keys('Adriana Melo')
    # raise NotImplementedError(u'STEP: When digito Adriana Melo no input')


@when(u'escolho no select a opção Artista')
def step_impl(context):
	context.element_selecionar = Select(context.web.find_element_by_id(element_selecionar))

	context.element_selecionar.select_by_value(value_selecionar_artista)
    # raise NotImplementedError(u'STEP: When escolho no select a opção Artista')


@then(u'devo ver a página do Artista')
def step_impl(context):
	context.web.implicitly_wait(25)

	context.get_nome_artista = context.web.find_element_by_xpath(get_nome_artista)

	nome_artista = context.get_nome_artista.text

	print(nome_artista)
    # raise NotImplementedError(u'STEP: Then devo ver a página do Artista')


@when(u'digito Frank Quitely no input')
def step_impl(context):
	context.element_pesquisar.send_keys('Frank Quitely')
    # raise NotImplementedError(u'STEP: When digito Frank Quitely no input')
