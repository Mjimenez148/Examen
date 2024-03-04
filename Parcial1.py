# INSTRUCCIONES
#Elabore un programa que contenga un menú, con el cual se manejará una cuenta de gastos. 
#Los datos son fecha de la transacción (modo string), tipo de transacción (d=débito-gasto, c=crédito-depósito), 
# monto. Las opciones del menú son: a. Agregar un depósito, b. Agregar un gasto.  c. Consultar saldo d. Salir. 
# Utilice listas con diccionarios.
from os import system
nombre =""
def mostrar_menu():
    print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
    print("OPCIONES")
    print("a. Agregar un deposito ")
    print("b. Agregar un gasto ")
    print("c. Consultar saldo ")
    print("d. Salir ")
    try:
        
        opcion = input("Escriba su opcion y presione ENTER: ")
        return opcion
    except ValueError:
        return 0
deposito=[]
saldo =0
print("Bienvenido a Banco PATITO")
nombre =input("Ingrese su nombre: ")
while True:
  system("cls")
  opcion=mostrar_menu()
  if opcion== "a":
      print("Agregar un deposito")
      fecha=input("Ingrese la fecha del deposito: ")
      monto =float(input("Ingrese el monto de deposito  "))
      saldo+=monto
      deposito.append({"Propietario: ":nombre,"Fecha: ": fecha, "Tipo: ":"Deposito","monto: ": monto,"Saldo: ":saldo})
      print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
      print("Propietario de la cuenta:  ", nombre)
      print("Tipo de Transaccion: Deposito")
      print("Fecha: ", fecha)
      print("Monto: ", monto)
      print("Saldo: ",saldo)
      input("precione ENTER para continuar...")
      print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
  elif opcion=="b":
      print("Agregar un gasto")
      fecha=input("Ingrese la fecha del gasto: ")
      monto =float(input("Ingrese el monto del gasto  "))
      saldo-=monto
      deposito.append({"Propietario: ":nombre,"Fecha: ": fecha, "Tipo: ":"Gasto","monto: ": monto,"Saldo: ":saldo})
      print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
      print("Propietario de la cuenta:  ", nombre)
      print("Tipode Transaccion: Gasto(Debito)")
      print("Fecha: ", fecha)
      print("Monto: ", monto)
      print("Saldo: ",saldo)
      input("precione ENTER para continuar...")
      print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
  elif opcion=="c":
      print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
      print("Consultar Saldo")
      print("Propietario de la cuenta:  ", nombre)
      print("Saldo : ", saldo)
      input("precione ENTER para continuar...")
  elif opcion=="d":
      print("Gracias por utilizar los servicios del Banco PATITO")
      break





