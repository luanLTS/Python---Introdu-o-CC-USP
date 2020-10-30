myCard = int(input("Digite o número do seu cartão de crédito: "))
nextCard = 1
foundCard = False

while nextCard != 0 and not foundCard:
    nextCard = int(input("Digite o número do próximo cartão: "))
    if nextCard == myCard:
        foundCard = True
if foundCard:
    print("UHUU!!!, found card :)")
else:
    print("NOOOO, not found card :(")