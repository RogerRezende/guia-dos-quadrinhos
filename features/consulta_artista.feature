#language: pt
Funcionalidade: Consultar Editora

	'''Eu como usuário quero acessar a página do Guia dos
	Quadrinhos para consultar os Artistas Adriana Melo e
	Frank Quitely'''

	Cenário: Consultar Adriana Melo no Guia dos Quadrinhos
	Dado acesso a página inicial do Guia dos Quadrinhos
	Quando clico no input de Pesquisar por
	E digito Adriana Melo no input
	E escolho no select a opção Artista
	E clico em Pesquisar
	Então devo ver a página do Artista

	Cenário: Consultar Frank Quitely no Guia dos Quadrinhos
	Dado acesso a página inicial do Guia dos Quadrinhos
	Quando clico no input de Pesquisar por
	E digito Frank Quitely no input
	E escolho no select a opção Artista
	E clico em Pesquisar
	Então devo ver a página do Artista