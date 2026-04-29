from dataclasses import dataclass, field
from datetime import datetime

class OutOfStockError(Exception):
    pass

@dataclass
class Product:
    id: int
    name: str
    price: float
    bestand: int = 0

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Preis nicht unter 0")
        if self.bestand < 0:
            raise ValueError("Bestand kann nicht unter 0 sein")

    def __str__(self):
        return f"{self.name} (ID: {self.id}) - Preis: {self.price:.2f}€ - Bestand: {self.stock}"

@dataclass
class PhysicalProduct(Product): 
    gewicht: float = 0.0
    shipping_costs: float = 0.0

    def __str__(self):
        return f"[Physisch] {super().__str__()} - Gewicht: {self.gewicht}kg"

@dataclass
class DigitalProduct(Product): 
    ablaufdatum: str = ""
    bestand: int = float('inf')

    def __str__(self):
        return f"[Digital] {super().__str__()} - Ablaufdatum: {self.ablaufdatum}"

@dataclass
class Warehouse: 
    def __init__(self):
        self.inventar = {} 
        self.verlauf = []

    def produkt_hinzufuegen(self, product: Product):
        self.inventar[product.id] = product
        self._eintrag(f"Hinzugefügt: {product.name}")

    def produkt_verkauf(self, product_id: int, quantity: int): 
        product = self.inventar.get(product_id) 
        if not product: return

        if product.bestand < quantity: 
            raise OutOfStockError(f"Nicht genug {product.name}!")

        if not isinstance(product, DigitalProduct):
            product.bestand -= quantity

        self._eintrag(f"Verkauf: {quantity}x {product.name}")

    def _eintrag(self, message: str): 
        timestamp = datetime.now().strftime("%H:%M:%S") 
        self.verlauf.append(f"[{timestamp}] {message}")

    @classmethod
    def json(cls, json_str: str): 
        return cls()

    @staticmethod
    def mehrwertsteuer(price: float): 
        return price * 0.19

    def filter_inventar(self):
        return list(filter(lambda p: p.bestand < 5, self.inventar.values()))