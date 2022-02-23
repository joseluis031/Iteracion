texto = input("Introduce el texto que deseas separar: ")
def separar_problemas(texto, separador):
  palabra = texto.split(separador)
  return palabra
print(separar_problemas(texto, in))