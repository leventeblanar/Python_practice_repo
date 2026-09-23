def filter_paid_orders(orders: list[dict]) -> list[dict]:
    return [order for order in orders if order["status"] == "paid"]

def sort_orders_by_key(orders: list[dict]) -> list[dict]:
    return sorted(orders, key=lambda order: (-order["total"], order["customer"]))

if __name__ == '__main__':

    orders = [
    {"id": 101, "customer": "Anna", "total": 15400, "status": "paid"},
    {"id": 102, "customer": "Béla", "total": 8900, "status": "pending"},
    {"id": 103, "customer": "Csaba", "total": 22100, "status": "paid"},
    {"id": 104, "customer": "Dóra", "total": 4700, "status": "cancelled"},
    {"id": 105, "customer": "Erika", "total": 22100, "status": "paid"},
    ]

    paid_orders = filter_paid_orders(orders)
    sorted_by_total = sort_orders_by_key(paid_orders)
    print(sorted_by_total)