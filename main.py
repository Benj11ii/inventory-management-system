# Importar módulos
from modulos.validaciones import validar_edad, validar_tipo_usuario
from modulos.menu import menu_cliente, menu_proveedor

#Funcion principal para iniciar el sistema
def main():
    print("Sistema de gestión de productos")
    print("*********************************")

    #Se pide el nombre de usuario
    nombre_usuario = input("Ingrese el nombre de usuario : ").strip().title()

    # Uso funciones de validación importadas
    edad = validar_edad()
    tipo_usuario = validar_tipo_usuario()

    # Redireccionaré según el rol si es cliente o proveedor
    if tipo_usuario == "Cliente":
        print(f"\n--- Bienvenido al Panel de Cliente ---")
        menu_cliente(nombre_usuario)
    elif tipo_usuario == "Proveedor":
        print(f"\n--- Bienvenido al Panel de Proveedor ---")
        menu_proveedor(nombre_usuario)

# Punto de ejecución para gatillar las demás funciones modulos
if __name__ == "__main__":
    main()