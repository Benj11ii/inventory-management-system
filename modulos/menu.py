# Se importan las funciones del otro archivo
from modulos.gestion_datos import (
    ingresar_producto_proveedor,
    mostrar_inventario,
    solicitar_producto_cliente,
    mostrar_solicitudes,
    buscar_producto
)

#Función para usar el menu del cliente, cuando este escriba cliente.
def menu_cliente(nombre):
    while True:
        print(f"\n--- Menú Cliente: {nombre} ---")
        print("1. Solicitar productos al vendedor")
        print("2. Ver mis solicitudes")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            res = solicitar_producto_cliente()
            if res:
                print("Solicitud enviada con éxito.")
        elif opcion == '2':
            mostrar_solicitudes()
        elif opcion == '3':
            print("Saliendo del menú.")
            break
        else:
            print("Opción no válida.")
#Función para usar el menu para proveedor cuando corresponda.
def menu_proveedor(nombre):
    while True:
        print(f"\n--- Menú Proveedor: {nombre} ---")
        print("1. Ingreso de productos")
        print("2. Revisión de inventario")
        print("3. Buscar producto")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            res = ingresar_producto_proveedor()
            if res:
                print(f"Producto {res['nombre']} agregado con éxito.")
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            print("Buscar producto")
            buscar_producto()
        elif opcion == '4':
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida.")