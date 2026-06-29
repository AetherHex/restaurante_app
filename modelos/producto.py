
class Producto:

    def __init__(self, nombre_producto: str, precio: float, tiempo_preparacion: int, disponible: bool):
        self.nombre_producto: str = nombre_producto
        self.precio: float = precio
        self.tiempo_preparacion: int = tiempo_preparacion
        self.disponible: bool = disponible

    def __str__(self):
        """Representación en texto del producto usando identificadores descriptivos."""
        estado_disponibilidad: str = "Disponible" if self.disponible else "Agotado"
        return f"{self.nombre_producto} | Precio: ${self.precio:.2f} | Tiempo: {self.tiempo_preparacion} min | [{estado_disponibilidad}]"

