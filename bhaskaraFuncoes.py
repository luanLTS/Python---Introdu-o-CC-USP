import math

def main():
    bhaskara(10, -1, 1)

def bhaskara (a, b, c):    
    delta(a, b, c)        

def delta(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "A equação não possui raízes reais."
    else:
        raizes(a, b, delta)

def raizes(a, b, delta):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if delta == 0:
        return f"A equação possui apenas um raíz real X = {x1}"
    else:
        return f"A equação possui duas raízes X1 = {x1} e X2 = {x2}"

main()  