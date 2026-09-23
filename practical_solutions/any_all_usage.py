def all_orders_paid(orders: list[dict]) -> bool:
    return all(order["paid"] for order in orders)

def has_large_order(orders: list[dict], limit: int) -> bool:
    return any(order["total"] > limit for order in orders)

if __name__ == '__main__':

    orders = [
    {"id": 101, "total": 15400, "paid": True},
    {"id": 102, "total": 8900, "paid": True},
    {"id": 103, "total": 22100, "paid": False},
    {"id": 104, "total": 4700, "paid": True},
    ]

    print(all_orders_paid(orders))
    print(has_large_order(orders, 20000))