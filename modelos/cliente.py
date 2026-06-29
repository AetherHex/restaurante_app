
class Cliente:

    def __init__(self, cedula: str, nombre_completo: str, numero_orden: int, visitas_realizadas: int, es_cliente_frecuente: bool):
        self.cedula: str = cedula
        self.nombre_completo: str = nombre_completo
        self.numero_orden: int = numero_orden
        self.visitas_realizadas: int = visitas_realizadas
        self.es_cliente_frecuente: bool = es_cliente_frecuente

    def __str__(self) -> str:
        tipo_cliente: str = "Frecuente (Aplica Descuento)" if self.es_cliente_frecuente else "Regular"
        return f"C.I.: {self.cedula} | {self.nombre_completo} | Historial: {self.visitas_realizadas} visitas | Tipo: {tipo_cliente}"
