while True:
 print ("Ingrese un NUMERO para saber si es par o impar")

 num1 = int(input("Ingrese un numero:"))
 op= num1 % 2

 def Resultado(op):
  if op  == 1:
   return "IMPAR" 
  elif op == 0:
   return "PAR"

 print(Resultado(num1 % 2))

