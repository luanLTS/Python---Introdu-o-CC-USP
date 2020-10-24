desc = True
ant = int(input("Digite o primeiro número da sequência: "))
valor = 1

while valor != 0 and desc == True:
    valor = int(input("Digite o próximo valor da sequência: "))
    if valor > ant:
        desc = False
    ant = valor

if desc:
    print("A sequência está em ordem decrescente :-)")
else:
    print("A sequência não está em ordem decrescente :-(")