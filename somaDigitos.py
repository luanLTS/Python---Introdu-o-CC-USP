n = int(input("Digite um intero com com mais de um dígito: \n"))
aux = len(str(n))
i = 0
soma = 0

while i <= aux:
    soma += (n % 10)
    n = n // 10
    i = i + 1

print("A soma dos dígitos é:",soma)