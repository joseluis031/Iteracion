# Iteracion
Trabajo realizado por José Luis Rodríguez y Claudia Lozano.
Dirección de Github: [GitHub](https://github.com/joseluis031/Iteracion.git)

## Ejercicio 6: Historial de una cuenta corriente

El código que hemos empleado en el ejercicio 6 es el que mostramos a continuación:

```operaciones = []
cuenta = input("Desea abrir una cuenta en el banco (si/no): ")

if cuenta == "no":
    print("Usted no desea abrir una cuenta en nustro banco. Muchas gracias.")
if cuenta == "si":
    saldo = 0
    print("Primero debe abonar dinero en la cuenta.")
    abono= int(input("Introduzca el dinera desea abonar:"))
    saldo = (abono).add(operaciones)

operacion = input("¿Desea hacer otra operación más como consultar dinero,retirar o abonar?")
if operacion == "no":
    print("Vale gracias por consultar este banco. Hasta pronto.")
if operacion == "abonar":
    introducir_dinero= float(input("Introduzca el dinero de desea ingresar en la cuenta: "))
    saldo = (saldo + introducir_dinero).add(operaciones)
    print("Su saldo es de " , saldo , "€")
if operacion == "consultar":
    print("El saldo de su cuenta es " , saldo , "€")
if operacion == "retirar":
    retirar_dinero= float(input("Introduzca el dinero que desea retirar: "))
    saldo = (saldo - retirar_dinero).add(operaciones)
    if saldo >= 0:
        print("Con la retirada de " , retirar_dinero , " su saldo disminuye a un total de " , saldo , "€")
    if saldo < 0:
        saldo = saldo * -1
        print("Con la retirada de " , retirar_dinero ,"Usted no tiene saldo en la cuenta, además debe un total de  " , saldo , "€")

suma= 20
if sum(operaciones) > suma: 
  print("La media de los importes de los movimientos es superior al mínimo establecido")
else:
  print("La media de los importes de los movimientos es inferior al mínimo establecido")
  ```

## Ejercicio 7: Edición de un número entero

El código que hemos empleado en el ejercicio 7 es el que mostramos a continuación:

```numero = int(input("Introduce un número: "))
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

  ```

## Ejercicio 8: Análisis de una cadena de caracteres

El código que hemos empleado en el ejercicio 8 es el que mostramos a continuación:

```
texto = input("Introduce el texto que deseas separar mediante (.): ")
n = len(texto)

separador = " . "
a = texto.split(".")

b = list(texto).count(".")
for numero in range (b+1):
  posicion_elemento = 1 + numero
print(posicion_elemento , " , " , a[numero])
```

## Ejercicio 9: Búsqueda de palabras en un diccionario

El código que hemos empleado en el ejercicio 9 es el que mostramos a continuación:

```
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
```

## Ejercicio 10: Representar los miembros de una familia

El código que hemos empleado en el ejercicio 10 es el que mostramos a continuación:

```elegir = input("Elige: euclides o sumas y rectas ")
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
  ```


## Ejercicio 11: mcd de dos números enteros

El código que hemos empleado en el ejercicio 11 es el que mostramos a continuación:




## Ejercicio 12: Cuadrados perfectos y raíz cuadrada entera

El código que hemos empleado en el ejercicio 12 es el que mostramos a continuación:

```
#importamos librerias
import math

a = input("Para obtener todos los cuadrados perfectos entre o y un número, introduce cuadrado, pero si dea realizar la raíz cuadrada de un número entero, introduce raiz: ")

if a == "cuadrado":
  def cuadrado1 (x,y):
    if (x**2) <= b:
      print(x**2)
      cuadrado1(0,int(input("Introduce el valos hasta el que deseas que llegue su lista de cuadrados: ")))

if a == "raiz":
  b=int(input("Introduce un número entero para el cual desee obtener su raíz cuadrada: "))
  raiz1 = b **(1/2)
  print("La raiz cuadrada de " , b , " es " , raiz1)

if a != "cuadrado" and a!= "raiz":
      print("Introduce un valor correcto.")
```