n = int(input("Digite un inteiro: "))
adj = False
dig = 1

digAnterior = n % 10
n = n // 10
while dig != 0 and not adj:
    dig = n % 10
    if dig == digAnterior:
        adj = True
    digAnterior = dig
    n = n // 10

if adj:
    print("O número digitado possui 2 dígitos adjascentes.")
else:
    print("O número digitado não possui 2 dígitos adjascentes.")