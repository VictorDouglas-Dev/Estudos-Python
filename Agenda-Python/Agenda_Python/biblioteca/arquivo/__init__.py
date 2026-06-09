from Agenda_Python.biblioteca.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[1;31mHouve um ERRO na criação do arquivo\033[m')
    else:
        print(f'\033[1;34Arquivo\033[m {nome} \033[1;34mcriado com sucesso.\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[1;31mERRO ao ler o arquivo\033[m')
    else:
        cabeçalho('[\033[1;35mEVENTOS DA AGENDA\033[m]')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', data=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[1;31mHouve um ERRO na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nome};{data}\n')
        except:
            print('\033[1;31mHouve um ERRO na hora de escrever os dados\033[m')
        else:
            print(f'\033[1;34mNovo Evento\033[m {nome} \033[1;34mAnotado.\033[m')
            a.close()

