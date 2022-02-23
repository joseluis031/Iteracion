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