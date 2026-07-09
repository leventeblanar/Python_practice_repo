from enum import Enum
from dataclasses import dataclass

class ProductCategory(Enum):
    ELECTRONICS = "electronics"
    OFFICE = "office"
    FURNITURE = "furniture"

@dataclass
class Product:
    name: str | None
    price: int
    category: ProductCategory

def basic_practice():

    product = Product(
        name="Laptop",
        price=300000,
        category=ProductCategory.ELECTRONICS
    )

    if product.category == ProductCategory.ELECTRONICS:
        print("Elektronikai termék")


        

basic_practice()