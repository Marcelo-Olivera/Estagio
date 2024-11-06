import json

# Carregando os dados do faturamento de um arquivo JSON
with open('Questao3/faturamento.json', 'r') as file:
    dados = json.load(file)

# Filtrando apenas os dias com faturamento acima de zero
faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calculando o menor e o maior faturamento diário
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Calculando a média mensal ignorando os dias sem faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# fazendo a conta do número de dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

# Resultados
print(f"Menor faturamento diário: {menor_faturamento}")
print(f"Maior faturamento diário: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
