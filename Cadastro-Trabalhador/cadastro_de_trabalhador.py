from utilidades.interface import cabeçalho, menu, linha, colorir, leiaInt, leiaFloat

from datetime import datetime
cabeçalho(colorir('[Cadastrar Funcionário]', 1))
dados = dict()
dados['nome'] = str(input(colorir('Nome: ', 1)))
nasc = leiaInt(colorir('Ano de Nascimento: ', 1))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = leiaInt(colorir('Carteira de Trabalho (0 não tem): ', 1))
if dados['ctps'] != 0:
    dados['contratação'] = leiaInt(colorir('Ano de Contratação: ', 1))
    dados['salário'] = leiaFloat(colorir('Salário: R$', 1))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
menu(dados)


