while True:
 print ("Hola, vamos a calcular su indice de masa corporal:")

 Peso= float (input("Por favor ingrese su peso en kg:"))
 Altura= float (input ("Por favor ingrese su altura:")) 

 Operacion= (input(Peso / Altura **2))
 if Operacion == '/': print (Peso / (Altura **2)) 

 print ("Su indice de masa corporal es: ", Peso / (Altura **2))


