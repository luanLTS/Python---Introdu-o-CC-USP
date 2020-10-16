seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dia = seg // 86400
segRestante = seg % 86400
hora = segRestante // 3600
segRestante = segRestante % 3600
minuto = segRestante // 60
segRestante = segRestante % 60

print(dia,"dias,",hora,"horas,",minuto,"minutos e",segRestante,"segundos.")