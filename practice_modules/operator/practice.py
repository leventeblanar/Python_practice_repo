from operator import attrgetter, itemgetter
from dataclasses import dataclass

@dataclass
class Order:
    order_id: int
    customer: str
    tota: int
    status: str


def itemgetterel():

    orders = [
        {"order_id": "ORD-1", "customer": "Anna", "total": 15480, "status": "completed"},
        {"order_id": "ORD-2", "customer": "Béla", "total": 5976, "status": "processing"},
        {"order_id": "ORD-3", "customer": "Csilla", "total": 18289, "status": "pending"},
        {"order_id": "ORD-4", "customer": "Dávid", "total": 6786, "status": "completed"},
    ]

    ordere_total_alapjan_csokkeno = sorted(orders, key=itemgetter("total"), reverse=True)
    legnagyobb_total_order = max(orders, key=itemgetter("total"))
    status_majd_total_alapjan = sorted(orders, key=itemgetter("status", "total"))

    print(ordere_total_alapjan_csokkeno)
    print(legnagyobb_total_order)
    print(ordere_total_alapjan_csokkeno)

def attrgetterel():

    orders = [
        Order(order_id = "ORD-1", customer = "Anna", total =  15480, status = "completed"),
        Order(order_id = "ORD-2", customer = "Béla", total =  5976, status = "processing"),
        Order(order_id = "ORD-3", customer = "Csilla", total =  18289, status = "pending"),
        Order(order_id = "ORD-4", customer = "Dávid", total =  6786, status = "completed"),
    ]

    orders_by_total_desc = sorted(orders, key=attrgetter("total"), reverse=True)
    max_total_order = max(orders, key=attrgetter("total"))
    orders_by_status_then_total = sorted(orders, key=attrgetter('status', 'total'))

    print(orders_by_total_desc)
    print(max_total_order)
    print(orders_by_status_then_total)