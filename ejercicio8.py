texto = input("Introduce el texto que deseas separar mediante (.): ")
n = len(texto)

separador = " . "
a = texto.split(".")

b = list(texto).count(".")
for numero in range (b+1):
  posicion_elemento = 1 + numero
print(posicion_elemento , " , " , a[numero])