while True:

 anho = int (input ("Vamos a verificar si un año es bisiesto. INGRESE UN AÑO: "))

 if anho % 4 == 0 and anho % 100 != 0 or anho % 400 == 0 :

    print (f"El año {anho} es BISIESTO")

 else:
    print (f"El año {anho} no es BISIESTO")




