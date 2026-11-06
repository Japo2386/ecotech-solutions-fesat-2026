
from pathlib import Path
import json


class StockInvalidoError(Exception):

    def __init__(self, mensaje="El stock no puede ser un valor negativo."):
        super().__init__(mensaje)


class DispositivoEcologico:

    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

        self._stock = 0
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError(
                f"Stock inválido para '{self.nombre}': {nuevo_stock}"
            )

        self._stock = nuevo_stock

    def generar_ficha_tecnica(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": f"${self.precio:.2f}",
            "stock": self.stock,
        }


class PanelSolar(DispositivoEcologico):

    def __init__(
        self, id_producto, nombre, precio,
        stock, eficiencia, potencia_w
    ):
        super().__init__(id_producto, nombre, precio, stock)

        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self):
        ficha = super().generar_ficha_tecnica()

        ficha.update({
            "tipo": "Panel Solar",
            "potencia_w": self.potencia_w,
            "eficiencia": f"{self.eficiencia}%",
        })

        return ficha


class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):

        catalogo = []

        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.generar_ficha_tecnica())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                catalogo,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(f"Catálogo guardado correctamente en: {ruta_archivo}")


def main():

    print("=" * 60)
    print("         ECOTECH SOLUTIONS - GESTIÓN DE INVENTARIO")
    print("=" * 60)

    panel = PanelSolar(
        1, "Panel Solar Eco 300W", 150000, 10, 21, 300
    )

    bateria = DispositivoEcologico(
        2, "Batería Ecológica", 85000, 5
    )

    print("\nVALIDACIÓN DE STOCK")
    print("-" * 60)

    try:
        panel.stock = -5

    except StockInvalidoError as error:
        print(f"Error controlado: {error}")

    print(f"Stock actual del panel: {panel.stock}")

    print("\nFICHAS TÉCNICAS")
    print("-" * 60)

    for dispositivo in [panel, bateria]:
        ficha = dispositivo.generar_ficha_tecnica()

        for clave, valor in ficha.items():
            print(f"{clave}: {valor}")

        print("-" * 60)

    print("\nEXPORTACIÓN DEL CATÁLOGO")
    print("-" * 60)

    gestor = GestorInventario()

    ruta_json = Path(__file__).resolve().parent / "catalogo_ecotech.json"

    gestor.guardar_catalogo_json(
    [panel, bateria],
    ruta_json
)
    print("\n" + "=" * 60)
    print("              FIN DEL PROCESAMIENTO")
    print("=" * 60)


if __name__ == "__main__":
    main()
