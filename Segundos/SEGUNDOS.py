print ("Vamos a calcular |Segundos|")

horas = int (input ("Ingresa la cantidad de horas: "))
minutos = int (input ("Ingresa la cantidad de minutos:"))
segundos = int (input ("Ingresa la cantidad de segundos: "))

segundos_desde_horas = horas * 3600
segundos_desde_minutos = minutos * 60

total_segundos = segundos_desde_horas + segundos_desde_minutos + segundos

print (f" El tiempo total equivale a: {total_segundos} segundos.")

