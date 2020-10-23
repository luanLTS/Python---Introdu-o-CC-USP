import math
x1 = int(input("Digite o valor para x1: \n"))
y1 = int(input("Digite o valor para y1: \n"))
x2 = int(input("Digite o valor para x2: \n"))
y2 = int(input("Digite o valor para y2: \n"))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d >= 10:
    print("longe")
else:
    print("perto")