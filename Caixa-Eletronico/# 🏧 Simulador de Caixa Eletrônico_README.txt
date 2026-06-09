# 🏧 Simulador de Caixa Eletrônico (ATM)

> Projeto desenvolvido em **Python** que simula a lógica de saque de um terminal bancário, calculando a distribuição otimizada de cédulas.

## 📋 Descrição do Programa
O sistema recebe um valor inteiro de saque e informa ao usuário exatamente quantas cédulas de cada valor serão entregues. O algoritmo prioriza as notas de maior valor para minimizar a quantidade de papel moeda entregue.

### Cédulas suportadas:
* R$ 50,00
* R$ 20,00
* R$ 10,00
* R$ 1,00

## 🛠️ Destaques Técnicos (Conceitos de ADS)
* **Modularização:** O código utiliza funções específicas (`linha` e `cabecalho`) para padronizar a interface visual.
* **Lógica de Algoritmos:** Implementação de divisão inteira para cálculo de quantidade e atualização do saldo restante.
* **Interface Colorida:** Uso de códigos de escape ANSI para criar uma experiência visual mais amigável no terminal.
* **Estrutura de Repetição:** Uso de um laço `for` para percorrer a lista de cédulas disponíveis.

## 📂 Estrutura de Arquivos
```text
caixa-eletronico-python/
└── caixa_eletronico.py # Script principal com a lógica de saque
