while True:    

 print ("Hola vamos a comparar numeros el dia de hoy, mayor o menor:")
 num1 = int (input("Ingrese numero a comparar:"))
 num2 = int (input("Ingrese 2do numero a comparar:"))

 def COMPARANDO (num1 , num2):
    if num1 > num2:
        return "El num 1 es mayor que el segundo "
    elif num1 < num2:
        return "El num 1 es menor que el seguno "


 print (COMPARANDO (num1 , num2))

 