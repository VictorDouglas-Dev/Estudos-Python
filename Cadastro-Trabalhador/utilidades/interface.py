def linha(tam=50, cor=2):
    return colorir('=' * tam, cor)


def cabeçalho(txt, cor=2):
    print(linha(cor=cor))
    print(txt.center(55))
    print(linha(cor=cor))


def colorir(msg, cor=0):
    """0: sem cor, 1: vermelho, 2: verde, 3: amarelo
    """
    cores = ('\033[m', '\033[1;31m', '\033[1;32m', '\033[1;33m')
    return f"{cores[cor]}{msg}{cores[0]}"


def menu(dados):
    cabeçalho(colorir('[Funcionário Cadastrado]', 1))
    for k, v in dados.items():
        exibir_valor = f"R${v:.2f}" if isinstance(v,float) else v
        nome_campo = f"{k:.<40}"
        print(f' - {colorir(nome_campo, 1 )}{exibir_valor}')
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(colorir('ERRO: Digite um número inteiro válido!', 3))
            continue
        else:
            return n
        

def leiaFloat(msg):
    while True:
        entrada = input(msg).replace(',','.').strip()
        try:
            n = float(entrada)
        except (ValueError, TypeError):
            print(colorir('ERRO: Digite um valor monetário/decimal válido!', 3))
            continue
        else:
            return n
        