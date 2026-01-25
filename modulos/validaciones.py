#Función para validar la edad, según rango etario
def validar_edad():
    while True:
        try:
            edad = int(input("Ingresa la edad de usuario (entre 18 y 99): "))

            if 18 <= edad <= 99:
                # Lógica requerida por el PDF
                if edad > 60:
                    print("Nota: Usuario categorizado como Adulto Mayor. 👴")
                elif edad < 30:
                     print("Nota: Usuario categorizado como Joven.")
                else:
                    print("Nota: Usuario categorizado como Adulto.")

                return edad
            else:
                print("Error: Solo ingresa valor entre 18 a 99.")

        except ValueError:
            print("Error: Debes ingresar un número entero.")
#Función para validar entre cliente o proveedor.
def validar_tipo_usuario():
    ROLES = ('Cliente', 'Proveedor')

    while True:
        tipo = input(f"Ingrese el tipo de usuario {ROLES}: ").strip().title()
        if tipo in ROLES:
            return tipo
        else:
            print(f"Error: Solo se permite {ROLES}. Intente de nuevo.")