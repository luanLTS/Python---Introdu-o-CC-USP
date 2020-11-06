import math

def main():
    bhaskara(-9, 15, 5)

def bhaskara (a, b, c):    
    delta(a, b, c)        

def delta(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("A equação não possui raízes reais.") 
    else:
        raizes(a, b, d)

def raizes(a, b, d):
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if delta == 0:
        print(f"A equação possui apenas um raíz real X = {x1}")
    else:
        print(f"A equação possui duas raízes X1 = {x1} e X2 = {x2}") 

main()