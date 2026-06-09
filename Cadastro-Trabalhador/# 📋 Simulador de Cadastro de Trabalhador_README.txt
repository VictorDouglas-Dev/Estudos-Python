# 📋 Simulador de Cadastro de Trabalhador (Python)

Este projeto é um sistema de registro profissional que utiliza lógica de programação para calcular dados previdenciários. Desenvolvido como parte dos meus estudos em **Análise e Desenvolvimento de Sistemas (ADS)**, o foco aqui foi a aplicação de **modularização** e **estruturas de dados (Dicionários)**.

---

## 🛠️ Funcionalidades

O script realiza a leitura de dados do trabalhador e processa as seguintes informações:
* **Cálculo de Idade:** Obtido automaticamente através do ano de nascimento.
* **Gestão de CTPS:** Se o usuário possuir Carteira de Trabalho, o sistema solicita:
    * Ano de contratação.
    * Salário atual (com formatação monetária).
* **Cálculo de Aposentadoria:** Informa com quantos anos o usuário irá se aposentar (baseado em 35 anos de contribuição).

---

## 🏗️ Estrutura Modular

Para manter o código limpo e organizado, o projeto foi dividido em módulos:

* `cadastro_de_trabalhador.py`: Arquivo principal com a lógica de negócio e cálculos.
* `utilidades/interface.py`: Módulo contendo funções de suporte para:
    * **Cores no Terminal:** Melhora a experiência visual do usuário.
    * **Validação de Dados:** Funções como `leiaInt()` e `leiaFloat()` para evitar erros de entrada.
    * **Formatação:** Cabeçalhos e linhas para organizar a exibição no console.

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/VictorDouglas-Dev/cadastro-trabalhador-python.git](https://github.com/VictorDouglas-Dev/cadastro-trabalhador-python.git)
