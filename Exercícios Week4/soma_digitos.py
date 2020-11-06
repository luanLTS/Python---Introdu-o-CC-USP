n = int(input("Digite um número inteiro: "))
aux = len(str(n))
i = 1
soma = 0
    
while i <= aux:
    ultDig = n % 10
    soma = soma + ultDig
    n = n // 10
    i+=1
print(soma)
'''
x = 123
print(x//10) retorna 12
print(x%10) retorna 3
'''