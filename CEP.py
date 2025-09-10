import requests

def consultar_cep(cep: str):
    cep = ''.join(filter(str.isdigit, cep))  # mantém só números

    if len(cep) != 8:
        return {"erro": "CEP inválido. Deve ter 8 dígitos."}

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            return {"erro": "CEP não encontrado."}
        return dados

    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro na requisição: {e}"}


def mostrar_resultado(dados):
    print("\nResultado da consulta:")
    print(f"CEP:         {dados['cep']}")
    print(f"Logradouro:  {dados['logradouro'] or '---'}")
    print(f"Bairro:      {dados['bairro'] or '---'}")
    print(f"Cidade:      {dados['localidade']}")
    print(f"Estado:      {dados['uf']}")


if __name__ == "__main__":
    while True:
        cep = input("\nDigite o CEP (somente números) ou 'sair': ").strip()
        if cep.lower() == "sair":
            print("Encerrando o programa.")
            break

        resultado = consultar_cep(cep)

        if "erro" in resultado:
            print(resultado["erro"])
        else:
            mostrar_resultado(resultado)

