#produto de uma sequência
tam = int(input("Digite o tamanho sa sequência: \n"))
i = 0
prod = 1

while i <= tam:
    valor = int(input("Digite o valor a ser multiplicado: "))
    prod = prod * valor
    i = i + 1

print("O produto dos valores digitados é:",prod)