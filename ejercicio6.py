operaciones = []
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

