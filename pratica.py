# 1. Dicionário: Ficha cadastral de um frete
frete = {"origem": "Fazenda Boa Vista", "peso": 4200, "valor_Tonelada": 150.00 }
# 2. Lista: Caminhões disponíveis no pátio
caminhoes = ["Scania R450", "Volvo FH16", "Mercedes Actros"]
# 3. Decisão (Condição): Checar o peso da carga
print("--- Analise de Transporte ---")
print("Primeiro caminhao da frota:")
print(caminhoes[0])
if frete["peso"] > 5000:
    print("Carga acima do limite permitido para transporte.")
else:
    print("Carga dentro do limite permitido para transporte.")
