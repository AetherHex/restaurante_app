# Sistema de Gestión de Restaurante Modularizado (restaurante_app)

**Asignatura:** Programación Orientada a Objetos  
**Semana 5:** Aplicación de Identificadores, Convenciones y Tipos de Datos Explícitos  
**Estudiante:** Tapia Cadena Aaron Alfonso

---

## 1. Descripción del Sistema
Este proyecto consiste en una aplicación modular en Python que representa un sistema básico de administración interna para un restaurante. La finalidad de esta entrega es demostrar el dominio técnico en la correcta asignación de identificadores semánticos, el uso de las convenciones de nombres estándar de la comunidad de Python (PEP 8), el tipado explícito de datos (Type Hinting) y la implementación práctica de estructuras compuestas (`list`) para el manejo de colecciones de objetos como productos y clientes.

## 2. Estructura Obligatoria del Repositorio
El proyecto se organiza respetando la estructura de paquetes y módulos requerida, incluyendo los archivos de inicialización correspondientes:

```text
restaurante_app/
├── modelos/
│   ├── __init__.py       # Inicializador del paquete de modelos.
│   ├── producto.py       # Modelo Producto con atributos tipados (str, float, int, bool).
│   └── cliente.py        # Modelo Cliente enfocado en la claridad de identificadores.
├── servicios/
│   ├── __init__.py       # Inicializador del paquete de servicios.
│   └── restaurante.py    # Servicio que procesa tipos de datos compuestos (listas).
└── main.py               # Orquestador del arranque y demostración del sistema.
