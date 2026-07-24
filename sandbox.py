from dataclasses import dataclass

@dataclass
class Order:
    id: int
    customer: str | None
    amount: int
    country: str

@dataclass
class Errors:
    row_id: int
    error: str

orders = [
    Order(id=1, customer="Anna", amount=12000, country="Hungary"),
    Order(id=2, customer="", amount=8000, country="Germany"),
    Order(id=3, customer="Béla", amount=0, country="Hungary"),
    Order(id=4, customer=None, amount=-500, country="Austria"),
    Order(id=5, customer="Csilla", amount=15000, country="Hungary"),
]

def validate_order(orders: list[Order]) -> tuple[list[dict], list[dict]]:

    valid_orders = []
    invalid_orders = []

    for index, order in enumerate(orders, 1):
        errors = []

        if not order.customer:
            errors.append("Missing customer")
        if order.amount <= 0:
            errors.append("Invalid order amount")

        if errors:
            invalid_orders.append({
                "row": index,
                "order": Order(order.id, order.customer, order.amount, order.country),
                "errors": Errors(index, errors),
            })
        else:
            valid_orders.append({
                "row": index,
                "order": Order(order.id, order.customer, order.amount, order.country),
            })

    return valid_orders, invalid_orders


if __name__ == '__main__':

    valid_orders, invalid_orders = validate_order(orders=orders)

    print(invalid_orders)