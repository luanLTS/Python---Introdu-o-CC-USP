def main():
    print(binomial(10, 6))

def fatorial(num):
    fat = 1
    i = 1
    while i <= num:
        fat *= i
        i+= 1
    return fat

def binomial(n, k):
    return int(fatorial(n)/ (fatorial(k) * fatorial(n - k)))

main()