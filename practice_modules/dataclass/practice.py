from dataclasses import dataclass

@dataclass
class Product:
    name: str | None
    price: int
    category: str

@dataclass
class ValidationResult:
    row: int
    product: Product
    errors: list[str]

def complete_validation(products: list[Product]) -> tuple[list[ValidationResult], list[ValidationResult]]:

    valid_product = []
    invalid_product = []

    for index, product in enumerate(products, 1):
        errors = []

        if not product.name:
            errors.append("hiányzó név")
        if product.price <= 0:
            errors.append("mínuszos/nullás ár")

        result = ValidationResult(
            row=index,
            product=product,
            errors=errors,
        )

        if result.errors:
            invalid_product.append(result)
        else:
            valid_product.append(result)

    return valid_product, invalid_product

    

def feladat_1():

    products = [
        Product(name="Laptop", price=300000, category="electronics"),
        Product(name="", price=150000, category="electronics"),
        Product(name="Mouse", price=8000, category="electronics"),
        Product(name="Keyboard", price=0, category="electronics"),
        Product(name=None, price=-100, category="office"),
    ]

    valid_products, invalid_products = complete_validation(products)

    print(valid_products)
    print(invalid_products)

feladat_1()