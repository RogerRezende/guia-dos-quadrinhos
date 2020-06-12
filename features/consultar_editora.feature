#language: pt
Funcionalidade: Consultar Editora

	'''Eu como usuário quero acessar a página do Guia dos
	Quadrinhos para consultar as Editoras Pipoca & Nanquim e
	Panini'''

	Cenário: Consultar Pipoca & Nanquim no Guia dos Quadrinhos
	Dado acesso a página inicial do Guia dos Quadrinhos
	Quando clico no input de Pesquisar por
	E digito Pipoca no input
	E escolho no select a opção Editora
	E clico em Pesquisar
	Então devo ver a página da Editora

	Cenário: Consultar Panini no Guia dos Quadrinhos
	Dado acesso a página inicial do Guia dos Quadrinhos
	Quando clico no input de Pesquisar por
	E digito Panini no input
	E escolho no select a opção Editora
	E clico em Pesquisar
	Então devo ver a página da Editora