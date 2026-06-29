from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

def main():
    # creamos el restaurante
    mi_restaurante = Restaurante("Sabor de Casa")
    # creamos los productos de comida
    primer_plato = Producto("Asado de Tira Familiar", 14.99, 25, True)
    segundo_plato = Producto("Ceviche de Camarón", 8.50, 15, True)
    postre_agotado = Producto("Volcán de Chocolate", 4.25, 10, False)

    # creamos los cliente
    primer_cliente = Cliente("1205432109", "Juan Perez Maldonado",1, 12, True)
    segundo_cliente = Cliente("0908765432", "Elena María Mendoza",1, 2, False)

    mi_restaurante.agregar_producto(primer_plato)
    mi_restaurante.agregar_producto(segundo_plato)
    mi_restaurante.agregar_producto(postre_agotado)

    mi_restaurante.registrar_cliente(primer_cliente)
    mi_restaurante.registrar_cliente(segundo_cliente)

    # imprimir menu
    print("=" * 72)
    print(f" MENU - {mi_restaurante.nombre_restaurante.upper()}")
    print("=" * 72)
    mi_restaurante.mostrar_catalogo_productos()

    # imprimir clientes
    print("=" * 72)
    print(f" CLIENTES - {mi_restaurante.nombre_restaurante.upper()}")
    print("=" * 72)
    mi_restaurante.mostrar_nomina_clientes()

if __name__ == "__main__":
    main()
