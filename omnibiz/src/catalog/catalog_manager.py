from decimal import Decimal
from .catalog_item import CatalogItem, Product, Service
 
 
class CatalogManager:
    def __init__(self, connection):
        self.connection = connection
 
    def add_product(
        self,
        product_name: str,
        description: str,
        price: Decimal,
        stock_quantity: int,
    ) -> int:
        product = Product(
            item_id=None,
            product_name=product_name,
            description=description,
            price= price,
            stock_quantity=stock_quantity,
            active=True,
        )
        return self._insert_item(product)
 
    def add_service(
        self,
        product_name: str,
        description: str,
        price: Decimal,
    ) -> int:
        service = Service(
            item_id=None,
            product_name=product_name,
            description=description,
            price=price,
            stock_quantity=0,
            active=True,
        )
        return self._insert_item(service)
 
    def get_item_by_id(self, item_id: int) -> CatalogItem | None:
        query = """
            SELECT item_id, product_name, description, price, stock_quantity, active
            FROM catalog
            WHERE item_id = %s
        """
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, (item_id,))
        row = cursor.fetchone()
        cursor.close()
 
        if row is None:
            return None
        return self._row_to_catalog_item(row)
 
    def list_active_items(self) -> list[CatalogItem]:
        query = """
            SELECT item_id, product_name, description, price, stock_quantity, active
            FROM catalog
            WHERE active = TRUE
            ORDER BY product_name
        """
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
 
        return [self._row_to_catalog_item(row) for row in rows]
 
    def update_item(
        self,
        item_id: int,
        product_name: str,
        description: str,
        price: Decimal,
        stock_quantity: int,
    ) -> bool:
        item = CatalogItem(
            item_id=item_id,
            product_name=product_name,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            active=True,
        )
 
        query = """
            UPDATE catalog
            SET product_name = %s,
                description = %s,
                price = %s,
                stock_quantity = %s
            WHERE item_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(
            query,
            (
                item.product_name,
                item.description,
                item.price,
                item.stock_quantity,
                item.item_id,
            ),
        )
        self.connection.commit()
        changed = cursor.rowcount > 0
        cursor.close()
        return changed
 
    def deactivate_item(self, item_id: int) -> bool:
        query = """
            UPDATE catalog
            SET active = FALSE
            WHERE item_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (item_id,))
        self.connection.commit()
        changed = cursor.rowcount > 0
        cursor.close()
        return changed
 
    def get_item_for_order(self, item_id: int) -> dict | None:
        item = self.get_item_by_id(item_id)
 
        if item is None or not item.active:
            return None
 
        return {
            "item_id": item.item_id,
            "product_name": item.product_name,
            "unit_price": item.price,
        }
 
    def _insert_item(self, item: CatalogItem) -> int:
        query = """
            INSERT INTO catalog
                (product_name, description, price, stock_quantity, active)
            VALUES
                (%s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(
            query,
            (
                item.product_name,
                item.description,
                item.price,
                item.stock_quantity,
                item.active,
            ),
        )
        self.connection.commit()
        item_id = cursor.lastrowid
        cursor.close()
        return item_id
 
    @staticmethod
    def _row_to_catalog_item(row: dict) -> CatalogItem:
        return CatalogItem(
            item_id=row["item_id"],
            product_name=row["product_name"],
            description=row["description"],
            price=row["price"],
            stock_quantity=row["stock_quantity"],
            active=bool(row["active"]),
        )