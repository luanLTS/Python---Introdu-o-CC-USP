#Soma de uma sequência
print("Digite uma sequência de valores terminada pro zero.")

valor = 1
soma = 0
while valor != 0:
    valor = int(input("Digite o valor a ser somado: \n"))
    soma = soma + valor

print("A soma dos valores digitados é: ",soma)
