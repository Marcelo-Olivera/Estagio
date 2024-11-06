import json

# Carregando os dados de faturamento por estado a partir do arquivo JSON
with open('Questao4/faturamentoEstado.json', 'r') as file:
    faturamento_estado = json.load(file)

# Calculando o faturamento total da distribuidora
faturamento_total = sum(faturamento_estado.values())

# Calculando o percentual de representação de cada estado
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estado.items()}

# Resultados
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
