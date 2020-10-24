import math
a = int(input("Digite o valor para A: \n"))
b = int(input("Digite o valor para B: \n"))
c = int(input("Digite o valor para C: \n"))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("A equação possui apenas um raíz real X =", x1)
    else:        
        print("A equação possui duas raízes X1 =", x1, "e X2 =", x2)