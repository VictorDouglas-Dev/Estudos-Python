# 📅 Agenda de Eventos com Persistência em Python

Este projeto é um sistema de gerenciamento de eventos desenvolvido em Python, focado em **modularização por pacotes**, **persistência de dados em arquivos de texto** e **robustez de software** através do tratamento de exceções.

O sistema permite que o usuário cadastre eventos que ficam salvos permanentemente em um arquivo `.txt`, garantindo que as informações não sejam perdidas ao fechar o programa.

## 🛠️ Destaques Técnicos

* **Persistência de Dados Inteligente:** O sistema possui lógica para verificar a existência do banco de dados local (`eventos.txt`) e criá-lo automaticamente caso não seja encontrado.
* **Tratamento de Exceções (Try/Except):** Implementação de validações para entradas de dados, lidando com erros de tipo (`ValueError`) e interrupções inesperadas (`KeyboardInterrupt`).
* **Modularização Profissional:** Organização do código em pacotes e submódulos (`interface` e `arquivo`), facilitando a manutenção.
* **Manipulação de Arquivos (I/O):** Uso técnico de `open()`, `read()` e `write()` com modos de acesso (`rt`, `wt+`, `at`).

## 📂 Estrutura do Projeto

```text
Agenda_Python/
├── sistema.py # Script principal (Entry Point)
└── biblioteca/ # Pacote principal de funções
    ├── arquivo/ # Módulo de persistência (.txt)
    └── interface/ # Módulo de UI e validação
