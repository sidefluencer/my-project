from dataclasses import dataclass
from decimal import Decimal
@dataclass
class CatalogItem:
    item_id: int | None
    product_name: str
    description: str
    price: Decimal
    stock_quantity: int
    active: bool = True
    def __post_init__(self):
        self.product_name = self.product_name.strip()
        self.description = self.description.strip()
        self.price = Decimal(str(self.price))
        if not self.product_name:
            raise ValueError("Product name must not be empty.")
        if self.price < 0:
            raise ValueError("Price must not be negative.")
        if self.stock_quantity < 0:
            raise ValueError("Stock quantity must not be negative.")
    def to_dict(self) -> dict:
        return {
            "item_id": self.item_id,
            "product_name": self.product_name,
            "description": self.description,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
            "active": self.active,
        }
@dataclass
class Product(CatalogItem):
    pass
@dataclass
class Service(CatalogItem):
    def __post_init__(self):
        super().__post_init__()
        if self.stock_quantity != 0:
            raise ValueError("Services must use stock_quantity 0.")