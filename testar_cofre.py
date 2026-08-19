import os
from dotenv import load_dotenv

print("--- Teste de Segurança ---")

# 1. O Python tranca a porta e abre o cofre silenciosamente (Lê o arquivo .env)
load_dotenv()

# 2. O Python pega apenas a chave que você pediu
chave_resgatada = os.getenv("MINHA_CHAVE_SECRETA")

# 3. Exibe a chave na tela só para provarmos que ele conseguiu ler
print("A chave secreta resgatada foi:", chave_resgatada)
