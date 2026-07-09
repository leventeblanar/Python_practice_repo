from dataclasses import dataclass
from enum import Enum

class ProductCategory(Enum):
    ELECTRONICS = "electronics"
    OFFICE = "office"
    FURNITURE = "furniture"

@dataclass
class Product:
    name: str | None
    price: int
    category: ProductCategory | str

@dataclass
class ValidationResult:
    row: int
    product: Product
    errors: list[str]

products = [
    Product(name="Laptop", price=300000, category=ProductCategory.ELECTRONICS),
    Product(name="", price=150000, category=ProductCategory.ELECTRONICS),
    Product(name="Mouse", price=8000, category=ProductCategory.ELECTRONICS),
    Product(name="Desk", price=70000, category=ProductCategory.FURNITURE),
    Product(name="Chair", price=0, category=ProductCategory.FURNITURE),
    Product(name=None, price=-100, category=ProductCategory.OFFICE),
    Product(name="Mystery item", price=5000, category="unknown"),
]

def validate_products(products: list[Product]) -> tuple[list[ValidationResult], list[ValidationResult]]:

    valid_products = []
    invalid_products = []

    for index, product in enumerate(products, 1):
        errors = []

        if not product.name:
            errors.append("Hiányzó név")
        if product.price <= 0:
            errors.append("Hibás ár")
        if not isinstance(product.category, ProductCategory):
            errors.append("Ismeretlen termék kategória")

        if errors:
            invalid_products.append(
                ValidationResult(
                    row=index,
                    product=product,
                    errors=errors,
                )
            )
        else:
            valid_products.append(
                ValidationResult(
                    row=index,
                    product=product,
                    errors=errors,
                )
            )

    return valid_products, invalid_products

def category_statistics(products: list[ValidationResult]):

    electronics = []
    electronics_counter = 0
    office = []
    office_counter = 0
    furniture = []
    furniture_counter = 0

    for row in products:
        if row.product.category == ProductCategory.ELECTRONICS:
            electronics_counter += 1
            electronics.append(row.product)
        if row.product.category == ProductCategory.OFFICE:
            office_counter += 1
            office.append(row.product)
        if row.product.category == ProductCategory.FURNITURE:
            furniture_counter += 1
            furniture.append(row.product)

    print(electronics)
    print(electronics_counter)
    print(office)
    print(office_counter)
    print(furniture)
    print(furniture_counter)



if __name__ == "__main__":
    valid_products, invalid_products = validate_products(products)

    print(valid_products)
    print(invalid_products)

    category_statistics(valid_products)