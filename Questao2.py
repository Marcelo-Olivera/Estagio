# Escolhendo o número a ser verificado
numero = int(input("Escolha um número: "))

# Inicio da sequência de Fibonacci
fibonacci = [0, 1]

# Gerando a sequência até que o último número seja igual ou maior que o número informado
while fibonacci[-1] < numero:
    proximo_valor = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_valor)

# Verificando se o número pertence à sequência
if numero in fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
