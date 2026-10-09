while True:
    print ("Vamos a verificar si un numero es mayor de dos numeros. |Por favor ingrese numero1 y numero2|: ")

    numero1= float (input("Ingrese el primer numero: "))
    numero2= float (input ("Ingrese el segundo numero: "))

    if numero1 > numero2:
        print (f"El numero mayor es: {numero1}")

    elif numero2 > numero1:
        print (f"EL numero mayor es: {numero2} ")

    else:
        print ("Ambos numeros son iguales.")

        
