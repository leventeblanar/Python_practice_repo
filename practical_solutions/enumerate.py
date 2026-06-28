def enumerate_items():

    products = [
        {"name": "Laptop", "price": 300000},
        {"name": "", "price": 150000},
        {"name": "Mouse", "price": 8000},
        {"name": "Keyboard", "price": 0},
        {"name": None, "price": -100},
    ]

    valid_products = []
    invalid_products = []

    for index, product in enumerate(products, 1):

        errors = []

        if not product["name"]:
            errors.append("missing name")
        if product["price"] <= 0:
            errors.append("invalid price")

        if errors:
            invalid_products.append({
                "row": index,
                "product name": product['name'],
                "errors": errors
            })
        else:
            valid_products.append({
                "row": index,
                "product name": product['name'],
            })

    print(valid_products)
    print(invalid_products)

enumerate_items()