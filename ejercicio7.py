numero = int(input("Introduce un número: "))
base = int(input("Introduce la base: "))

def edit(numero,base):
  if base > 36:
    print(numero)
  elif base < 2:
    print("esta base no esta permitida")
  else:
    if numero//base ==0:
      print(numero%base)
    else:
      numero = numero//base
    edit(numero, base)
edit(numero, base)
    