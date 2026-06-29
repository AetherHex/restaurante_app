from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_restaurante: str):
        # nombre del Restaurante
        self.nombre_restaurante: str = nombre_restaurante
        # lista
        self.productos_registrados: list = []
        self.clientes_registrados: list = []

    def agregar_producto(self, producto):
        self.productos_registrados.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes_registrados.append(cliente)

    def mostrar_catalogo_productos(self):
        print(f"\nMenu del restaurante: {self.nombre_restaurante.upper()}")
        if not self.productos_registrados:
            print("No hay productos dados de alta en el menú")
        for contador, producto_iterado in enumerate(self.productos_registrados, 1):
            print(f" {contador}. {producto_iterado}")

    def mostrar_nomina_clientes(self):
        print("\nClientes registrados")
        if not self.clientes_registrados:
            print("No se encuentran clientes registrados en el sistema.")
        for cliente_iterado in self.clientes_registrados:
            print(f" -> {cliente_iterado}")

