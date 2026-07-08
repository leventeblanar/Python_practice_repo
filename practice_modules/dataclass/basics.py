from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int

def basic_use():

    product = Product(name="Laptop", price=300000)

    print(product)
    print(product.name)
    print(product.price)

def in_use():

    products = [
        Product(name="Laptop", price=300000),
        Product(name="", price=150000),
        Product(name="Keyboard", price=0),
    ]

    hibas_products = []
    valid_products = []

    for index, product in enumerate(products, 1):
        errors = []

        if not product.name:
            errors.append("missing name")

        if product.price <= 0:
            errors.append("invalid price")

        if errors:
            hibas_products.append({
                "row": index,
                "errors": errors
            })
        else:
            valid_products.append({
                "row": index,
                "data": product
            })

    print(hibas_products)
    print(valid_products)

in_use()