elegir = input("Elige: euclides o sumas y rectas ")
x= int(input("Introduce el valor del divisor: "))
y= int(input("Introduce el valor del divisor: "))

if elegir == "euclides":
  def mcd(x, y):
    if y == 0:
     return x
    return mcd(y, x%y)
  final = mcd(x, y)
  print(final)

elif elegir == "sumas y rectas":
  def mcd(x, y):
    if x ==0 :
      return y
    elif y == 0:
      return x
    elif x == y:
      return x
    elif x > y:
      return mcd(x-y, y)
    return mcd(x, y-x)
  if(mcd(x, y)):
    final = mcd(x, y)
    print(final)
else:
  print("No existe m.c.d")
  

     