tempoDeJogo = int(input("Quanto tempo temos já jogado? \n"))

if tempoDeJogo < 90:
    print("Ainda resta", 90 - tempoDeJogo, "de jogo")
else:
    print("Puts está acabando o jogo")
    print("Apita logo juiz")