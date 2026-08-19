import requests

# 1. O endereço da API (onde vamos bater na porta)
url = "https://viacep.com.br/ws/01001000/json/"

# 2. A requisição GET (Pedindo os dados para o servidor externo)
resposta = requests.get(url)

# 3. Transformando a resposta (JSON) em um Dicionário Python
dados = resposta.json()

# 4. Acessando e imprimindo dados específicos pelas chaves
print("--- Resultado da Consulta na API ---")
print("Rua:", dados["logradouro"])
print("Bairro:", dados["bairro"])
print("Cidade:", dados["localidade"])
print("Status do Servidor:", resposta.status_code)