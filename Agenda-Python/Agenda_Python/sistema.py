from Agenda_Python.biblioteca.arquivo import *
from Agenda_Python.biblioteca.interface import *
from time import sleep

arq = 'eventos.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['[VER AGENDA]', '[CADASTRAR EVENTO]', '[SAIR]'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # Opçao de cadastrar uma novo evento.
        cabeçalho('[\033[1;35mCADASTRAR NOVO EVENTO\033[m]')
        nome = str(input('\033[1;35mEVENTO\033[m: '))
        data = leiaInt('\033[1;35mDIA\033[m: ')
        cadastrar(arq, nome, data)
    elif resp == 3:
        # Opção de sair do sistema.
        cabeçalho('<<< \033[1;35mSAINDO DA AGENDA\033[m >>>')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
        sleep(2)

