import sys
a = []
def añadir_palabra():
  palabra = str(input("Palabra para el diccionario: "))
  a.append(palabra)
  print(a)
  eleccion1=str(input("¿Quieres introducir más palabras? (si/no)"))
  if eleccion1 == "si":
    añadir_palabra()
  if eleccion1 == "no":
    nueva_eleccion()
def quitar_palabra():
    palabra_quitar= str(input("¿Qué palabra quieres eliminar?"))
    a.remove(palabra_quitar)
    print(a)
    nueva_eleccion()
def ordenar_palabra():
  orden=str(input("¿Quieres ordenar la lista? si o no"))
  if orden == "si":
    a.sort()
  else:
    sys.exit #para cerrar el programa
def nueva_eleccion():
  eleccion= str(input("¿Qué quieres hacer? añadir, eliminar, ordenar o terminar"))
  if eleccion == "añadir":
    añadir_palabra()
  if eleccion == "eliminar":
    quitar_palabra()
  if eleccion == "ordenar":
    ordenar_palabra()
  if eleccion == "terminar":
    sys.exit #para cerrar el programa
añadir_palabra()