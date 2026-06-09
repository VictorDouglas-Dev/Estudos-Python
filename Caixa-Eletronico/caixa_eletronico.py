def linha(tam=45):
    return '\033[1;35m=\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def saque(valor):
    for cédula in [50, 20, 10, 1]:
        quantidade = valor // cédula
        valor %= cédula
        if quantidade > 0:
            print(f'\033[1;32m{quantidade}\033[m \033[1;33mcédula(s)\033[m de \033[1;32mR${cédula}\033[m')
            print(linha())



    # Programa Principal
cabeçalho('[\033[1;33mBANCO VDSS\033[m]')
valor_usuario = int(input("\033[1;34mQual é o valor que você quer sacar?\033[m] \033[1;32mR$\033[m"))
saque(valor_usuario)
