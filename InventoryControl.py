import random
import os

#El git funciona
def menu():
    os.system ("cls") 
    print("1 - Mostrar inventario")
    print("2 - Agregar Producto")
    print("3 - Eliminar Producto")
    print("4 - Modificar cantidad")
    print("5 - Salir")

def EnterWait():
    input("Presione Enter para continuar...")

def mostrarInventario():
    os.system ("cls")
    if len(inventario) == 0:
        print("No hay nada en el inventario")
        EnterWait()
        return
    else:
        print("Inventario:")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")
        EnterWait()

def AgregarProducto():
    producto = input("Ingrese el producto: ")
    cantidad = input("Ingrese la cantidad: ")
    inventario.update({producto: cantidad})
    print("Producto añadido")
    EnterWait()


valorMenu = 0
inventario = {}

while valorMenu != 5:
    menu()
    valorMenu = int(input("Ingrese el valor del menu: "))
    if valorMenu == 1:
        mostrarInventario()
    elif valorMenu == 2:
        AgregarProducto()