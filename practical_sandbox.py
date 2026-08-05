from dataclasses import dataclass

def dict_grouping_gyak():
    sales = [
        {"country": "Hungary", "amount": 12000},
        {"country": "Germany", "amount": 8000},
        {"country": "Hungary", "amount": 15000},
        {"country": "Austria", "amount": 5000},
        {"country": "Germany", "amount": 22000},
        {"country": "Hungary", "amount": 3000},
    ]

    statistics = {}

    for sale in sales:
        country = sale["country"]
        amount = sale["amount"]

        if country not in statistics:
            statistics[country] = {
                "count": 1,
                "total_amount": amount,
            }
        else:
            statistics[country]["count"] += 1
            statistics[country]["total_amount"] += amount

    statistics_list = []

    for country, statistic in statistics.items():
        statistics_list.append({
            "country": country,
            "count": statistic["count"],
            "total_amount": statistic["total_amount"]
        })

    print(sorted(statistics_list, key= lambda row: row["total_amount"], reverse=True))


def enumerate_validation_error_handle():

    @dataclass
    class Product:
        name: str | None
        price: int
        stock: int

    @dataclass
    class ValidationResult:
        row: int
        product: Product
        errors: list[str]

    products = [
        {"name": "Laptop", "price": 300000, "stock": 5},
        {"name": "", "price": 12000, "stock": 3},
        {"name": "Mouse", "price": 0, "stock": 10},
        {"name": "Keyboard", "price": 25000, "stock": -2},
        {"name": None, "price": -5000, "stock": 0},
        {"name": "Monitor", "price": 90000, "stock": 2},
    ]

    valid_products = []
    invalid_products = []

    for index, product in enumerate(products, 1):

        errors = []

        if not product["name"]:
            errors.append("Missing name")
        if product["price"] <= 0:
            errors.append("Invalid price")
        if product["stock"] < 0:
            errors.append("No stock")

        result = ValidationResult(
            row=index,
            product=Product(
                name=product["name"],
                price=product["price"],
                stock=product["stock"],
            ),
            errors=errors,
        )

        if errors:
            invalid_products.append(result)
        else:
            valid_products.append(result)

    print(valid_products)
    print(invalid_products)

enumerate_validation_error_handle()