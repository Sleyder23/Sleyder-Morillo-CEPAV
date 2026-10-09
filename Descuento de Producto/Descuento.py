while True:
 print ("Hola vamos a calcular el descuento de tu producto:")

 Precio= float (input ("Ingrese el precio de su productor por favor:"))
 Descuento= float (input ("Ingrese el porcentaje de descuento a su productor por favor:"))

 MontoDescuento = Precio * Descuento / 100

 def Resultado (Precio, Descuento, MontoDescuento):
    if MontoDescuento > 0:
        print (f"El monto de descuento es: {MontoDescuento}")
    else:
        print ("No hay descuento para este producto.")


 Resultado (Precio, Descuento, MontoDescuento)