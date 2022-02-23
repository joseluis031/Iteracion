#definimos la variable del máximo común divisor de euclides.

x= input("Introduce el valor del divisor: ")
y= input("Introduce el valor del divisor: ")
mcd = x/y
if mcd == 0:
  print("El máximo común divisor es " , y , ".")
if mcd != 0:
  resto= x%y
  mcd_euclidesnuevo = y / resto
      