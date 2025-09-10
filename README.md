# Consulta de CEP com ViaCEP

Projeto simples em Python que consulta endereços usando a API
pública do [ViaCEP](https://viacep.com.br/).

------------------------------------------------------------------------

## Funcionalidades

-   Consulta informações de um CEP digitado pelo usuário.
-   Valida se o CEP possui 8 dígitos.
-   Exibe dados formatados: logradouro, bairro, cidade e estado.
-   Permite várias consultas em sequência.
-   Trata erros de conexão e CEP inexistente.

------------------------------------------------------------------------

## Tecnologias usadas

-   [Python 3](https://www.python.org/)
-   [Requests](https://pypi.org/project/requests/) (para consumo da API)

------------------------------------------------------------------------

## Instalação

Clone este repositório ou baixe os arquivos:

``` bash
git clone https://github.com/seu-usuario/consulta-cep.git
cd consulta-cep
```

Instale as dependências:

``` bash
pip install requests
```

------------------------------------------------------------------------

## Como usar

Execute o programa no terminal:

``` bash
python CEP.py
```

Digite o CEP (somente números) quando solicitado:

    Digite o CEP (somente números) ou 'sair': 01001000

    Resultado da consulta:
    CEP:         01001-000
    Logradouro:  Praça da Sé
    Bairro:      Sé
    Cidade:      São Paulo
    Estado:      SP

------------------------------------------------------------------------



## Melhorias futuras

-   Interface gráfica (Tkinter).
-   Suporte a múltiplos CEPs de uma lista.

------------------------------------------------------------------------


