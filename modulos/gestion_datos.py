# Estas serán las variables globales del módulo
lista_productos_solicitar = []
lista_productos = []
nombres_productos_registrados = set()

#Definición para ingresar producto desde el lado proveedor
def ingresar_producto_proveedor():
    print("\n--- Formulario de Ingreso para proveedor ---")
    nombre = input("Ingrese nombre del producto : ").strip().title()

    # Validación con SET, si existe un producto ya ingresado marcará error
    if nombre in nombres_productos_registrados:
        print("¡Error! Este producto ya existe en el inventario.")
        return None  # Retornamos vacío para indicar fallo

    # Se utiliza el try para capturar si existe algún error
    try:
        precio = float(input("Ingrese valor unitario en pesos : "))
        categoria = input("Ingrese categoría del producto : ").strip().title() #Usé strip para limpiar ingresos de espacios vacios, y title para poner la primera letra en mayuscula
        cantidad = int(input("Ingrese cantidad : "))
    except ValueError:
        print("Error en los datos numéricos.")
        return None

    precio_total = 0
    if precio > 0:
        precio_total = precio * cantidad
        print(f"El costo total de productos sería : {precio_total}")

    # Se agrega al SET para proteger duplicados futuros
    nombres_productos_registrados.add(nombre)

    # Guardo precio_total en el diccionario
    nuevo_prod = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio_total": precio_total
    }
    lista_productos.append(nuevo_prod)
    return nuevo_prod

#Funcion para solicitud del producto que realiza el cliente.
def solicitar_producto_cliente():
    print("\n--- Solicitud de Producto ---")
    nombre = input("Ingrese nombre del producto a solicitar: ").strip().title()
    categoria = input("Categoría: ").strip().title()

    solicitud = {"nombre": nombre, "categoria": categoria}
    lista_productos_solicitar.append(solicitud)
    return solicitud #retorno de la solicitud para usarla a posterior

#Función para mostrar el inventario
def mostrar_inventario():
    if not lista_productos:
        print("\nLa lista está vacía. No ha ingresado productos.")
    else:
        print("\n--- Inventario Actual ---")
        for i, prod in enumerate(lista_productos, 1):
            # Formateo de precios
            p_unit = f"${int(prod['precio']):,}".replace(",", ".")
            p_tot = f"${int(prod['precio_total']):,}".replace(",", ".")

            print(f"{i}. {prod['nombre']} | Precio: {p_unit} | Cantidad: {prod['cantidad']} | Total: {p_tot}")
        print(f"Total productos: {contar_productos_recursivo(lista_productos)}")


#Función para mostrar solicitudes del cliente.
def mostrar_solicitudes():
    if not lista_productos_solicitar:
        print("\nNo hay solicitudes pendientes.")
    else:
        print("\n--- Productos solicitados por clientes ---")
        for i, prod in enumerate(lista_productos_solicitar, 1):
            print(f"{i}. Producto: {prod['nombre']} | Categoría: {prod['categoria']}")

# Agregué un buscador de productos
def buscar_producto():
    print("\n--- Buscar Producto ---")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().title()

    # Se recorre la lista para ver si se encuentra
    encontrado = False
    for prod in lista_productos:
        if prod['nombre'] == nombre_buscar:
            print(f"¡Encontrado! Precio: ${prod['precio']} | Stock: {prod['cantidad']}")
            encontrado = True
            break

    #Mensaje si no lo detecta
    if not encontrado:
        print("Producto no encontrado en el inventario.")

def contar_productos_recursivo(lista, index=0):
    if index == len(lista):
        return 0
    return 1 + contar_productos_recursivo(lista, index + 1)