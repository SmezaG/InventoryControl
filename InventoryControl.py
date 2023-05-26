import random
import os

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
    os.system ("cls")
    producto = input("Ingrese el producto: ")
    cantidad = input("Ingrese la cantidad: ")
    inventario.update({producto: cantidad})


def EliminarProducto():
    os.system ("cls")
    producto = input("Que producto quiere eliminar?: ")
    for valor in inventario.keys():
        if valor == producto:
            del inventario[producto]
            return
    print("No se encontro el producto")
    EnterWait()

def ActualizaCantidad():
    os.system ("cls")
    producto = input("Que producto quiere modificar?: ")
    for valor in inventario.keys():
        if valor == producto:
            cantidad = input("Ingrese la nueva cantidad: ")
            inventario[producto] = cantidad
            return  
       
    print("No se encontro el producto")
    EnterWait()

valorMenu = 0
inventario = {}

while valorMenu != 5:
    os.system ("cls")
    menu()
    try:
        valorMenu = int(input("Ingrese el valor del menu: "))
    except ValueError:
        print("Debes introducir un número")
        EnterWait()

    
    if valorMenu == 1:
        mostrarInventario()
    elif valorMenu == 2:
        AgregarProducto()
    elif valorMenu == 3:
        EliminarProducto()
    elif valorMenu == 4:
        ActualizaCantidad()