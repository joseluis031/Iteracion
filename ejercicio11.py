""#definimos la variable del máximo común divisor de euclides.
elegir = input("Elige: Euclides o sumas y rectas ")
x= int(input("Introduce el valor del divisor: "))
y= int(input("Introduce el valor del divisor: "))
if elegir == "euclides":
  def mcd(x, y):
    if mcd == 0:
     print("El máximo común divisor es " , y , ".")
    if mcd != 0:
     resto= x%y
    mcd_euclidesnuevo = y / resto

elif elegir == "sumas y rectas":
   def mcd(x, y):
    if x ==0 :
      return y
    elif y == 0:
      return x
    elif x == y:
      return x
    elif x > y:
      return mcd(x, y-x)
    return mcd(x, y-x)
    else:
      print("")
  

     