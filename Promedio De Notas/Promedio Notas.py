while True:
 print ("Soy Tu Calculadora de Promedios en Notas. |Por favor ingrese las notas|: ")

 nota1 = float (input ("INGRESA LA 1ERA NOTA: "))
 nota2 = float (input ("INGRESA LA 2DA NOTA: "))
 nota3 = float (input ("INGRESA LA 3RA NOTA: "))

 promedio = (nota1+nota2+nota3) /3

 print (f"El promedio final es: {promedio:.2}")

 if promedio >= 6.0:
  print ("FELICIDADES HAS APROBADO LA MATERIA")

 else:
  print ("NO TIENES LA NOTA MINIMA PARA APROBAR LA MATERIA...")

  