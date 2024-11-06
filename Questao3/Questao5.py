# Escolhendo uma palavra para inverter
string_original = input("Digite uma palavra: ")

# Variável para armazenar a palavra invertida
string_invertida = ""

# Loop para construir a palavra invertida
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

# Resultado
print("String invertida:", string_invertida)
