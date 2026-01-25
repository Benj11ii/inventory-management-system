# Sistema de Gestión de Productos 🧾🐍

## Descripción del proyecto

Este proyecto corresponde al **Proyecto del Módulo 3** y consiste en el desarrollo de un **Sistema de Gestión de Productos** implementado en Python, aplicando los conceptos fundamentales del lenguaje vistos durante el módulo.

El sistema permite gestionar productos mediante una estructura modular, diferenciando roles de usuario (Cliente y Proveedor), validando datos ingresados y manipulando información mediante distintas estructuras de datos.

El objetivo principal es demostrar el uso correcto de:

* Estructuras de control
* Funciones
* Estructuras de datos
* Modularización
* Buenas prácticas de programación

---

## Funcionalidades principales

### 🔐 Validación de usuarios

* Ingreso de nombre de usuario.
* Validación de edad (rango entre 18 y 99 años).
* Clasificación etaria automática:

  * Joven
  * Adulto
  * Adulto Mayor
* Validación de tipo de usuario:

  * Cliente
  * Proveedor

---

### 👤 Menú Cliente

El usuario con rol **Cliente** puede:

* Solicitar productos indicando nombre y categoría.
* Visualizar el listado de productos solicitados.
* Salir del sistema mediante un menú iterativo.

---

### 🧑‍💼 Menú Proveedor

El usuario con rol **Proveedor** puede:

* Ingresar nuevos productos al inventario.
* Evitar el ingreso de productos duplicados mediante un conjunto (set).
* Visualizar el inventario completo.
* Buscar productos por nombre.
* Salir del sistema mediante un menú iterativo.

---

## Estructura del proyecto

```
DesarrolloModulo3/
│
├── main.py
│
├── modulos/
│   ├── __init__.py
│   ├── validaciones.py
│   ├── gestion_datos.py
│   └── menu.py
│
└── README.md
```

---

## Descripción de los módulos

### 📌 main.py

Archivo principal del sistema.

* Funciona como punto de entrada del programa.
* Captura datos iniciales del usuario.
* Llama a las funciones de validación.
* Redirecciona al menú correspondiente según el rol del usuario.

---

### 📌 modulos/validaciones.py

Contiene funciones encargadas de validar la información ingresada:

* Validación de edad con control de errores.
* Clasificación del usuario según rango etario.
* Validación del tipo de usuario mediante tuplas.

---

### 📌 modulos/gestion_datos.py

Encargado de la gestión de datos del sistema:

* Manejo de productos mediante listas y diccionarios.
* Uso de conjuntos (set) para evitar duplicados.
* Ingreso y solicitud de productos.
* Visualización de inventario y solicitudes.
* Búsqueda de productos por nombre.
* Contador de productos.


---

### 📌 modulos/menu.py

Implementa los menús interactivos del sistema:

* Menú para Cliente.
* Menú para Proveedor.
* Uso de ciclos `while` para interacción continua.
* Uso de condicionales y control de flujo.

---

## Estructuras de datos utilizadas

* **Listas (`list`)**: almacenamiento de productos y solicitudes.
* **Diccionarios (`dict`)**: representación de productos y solicitudes en pares clave-valor.
* **Tuplas (`tuple`)**: definición de roles de usuario.
* **Conjuntos (`set`)**: prevención de productos duplicados.

---

## Tecnologías y herramientas

* Lenguaje: **Python 3**
* Editor de código: **Pycharm**
* Control de errores con `try/except`
* Uso de f-strings para formateo de salida

---

## Buenas prácticas aplicadas

* Código modular y reutilizable.
* Uso de nombres de variables descriptivos.
* Separación clara de responsabilidades por módulo.
* Comentarios explicativos para facilitar la comprensión.
* Cumplimiento de las recomendaciones básicas de PEP 8.

---

## Conclusión

Este proyecto demuestra la aplicación práctica de los contenidos del Módulo 3, integrando validaciones, control de flujo, estructuras de datos y modularización. El sistema es funcional, escalable y puede ser extendido con nuevas características en futuros módulos.


---

🚀 ¡Proyecto desarrollado como parte del proceso de formación en Python!
