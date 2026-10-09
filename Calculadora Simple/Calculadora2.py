while True:
 print ("Bienvenido a la calculadora simple de SM")


 a = float (input ("Introduce valor 1 aca:"))
 b = float (input("Introduce valor 2 aca:"))

 operacion = input ("introduce la operacion a realizar (+ , -, *, ÷):")

 if operacion == '+':
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")

 elif operacion == '-':
    resultado = a - b
    print(f"El resultado de la resta es: {resultado}")

 elif operacion == '*':
    resultado = a * b
    print(f"El resultado de la multiplicación es: {resultado}")

 elif operacion == '÷':
    if b != 0:
        resultado = a / b
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")

 else:
    print("Operación no válida. Por favor introduce +, -, * o ÷.")      

    