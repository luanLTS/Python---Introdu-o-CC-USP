def main():
    num = int(input("Digite um inteiro"))
    i = 2
    fatorial = 1
    while i <= num:
        fatorial = fatorial * i
        i = i + 1
    
    print(fatorial)
main()