# Sistema de Gestión de Restaurante Modularizado (restaurante_app)

**Asignatura:** Programación Orientada a Objetos  
**Semana 5:** Aplicación de Identificadores, Convenciones y Tipos de Datos Explícitos  
**Estudiante:** Tapia Aaron 

---

## 1. Descripción del Sistema
Este proyecto consiste en una aplicación modular en Python que representa un sistema básico de administración interna para un restaurante. La finalidad central de esta entrega es demostrar el dominio técnico en la correcta asignación de identificadores semánticos, el uso estricto de las convenciones de nombres (PEP 8), el tipado explícito de datos y la implementación de listas para el manejo de colecciones de objetos.

## 2. Estructura del Proyecto
El software aplica una arquitectura modular que incluye archivos de inicialización de paquetes:

* `modelos/__init__.py`: Inicializador del paquete de modelos.
* `modelos/producto.py`: Modelo Producto con atributos tipados (str, float, int, bool).
* `modelos/cliente.py`: Modelo Cliente enfocado en la claridad de identificadores.
* `servicios/__init__.py`: Inicializador del paquete de servicios.
* `servicios/restaurante.py`: Servicio que procesa tipos de datos compuestos (listas).
* `main.py`: Punto de entrada que orquesta la ejecución.

## 3. Matriz de Identificadores y Tipos de Datos Utilizados

| Clase (PascalCase) | Atributo (snake_case) | Tipo de Dato |
| :--- | :--- | :--- |
| **Producto** | `nombre_producto` | `str` |
| | `precio_unitario` | `float` |
| | `tiempo_preparacion_minutos` | `int` |
| | `disponible` | `bool` |
| **Cliente** | `cedula_identidad` | `str` |
| | `nombre_completo` | `str` |
| | `visitas_realizadas` | `int` |
| | `es_cliente_frecuente` | `bool` |
| **Restaurante** | `nombre_establecimiento` | `str` |
| | `lista_productos_menu` | `list[Producto]`|
| | `lista_clientes_registrados`| `list[Cliente]` |

## 4. Reflexión sobre Buenas Prácticas
Utilizar identificadores descriptivos, tipos de datos adecuados y listas en un proyecto modular es fundamental porque garantiza la legibilidad, escalabilidad y seguridad del código. El tipado explícito actúa como una documentación viva que previene errores lógicos, mientras que el respeto a las convenciones (PascalCase y snake_case) permite que cualquier desarrollador pueda integrarse al proyecto comprendiendo la función exacta de cada variable y método al primer vistazo.
