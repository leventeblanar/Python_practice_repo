from itertools import groupby
from operator import itemgetter

orders = [
    {"order_id": "ORD-1", "customer": "Anna", "total": 15480, "status": "completed"},
    {"order_id": "ORD-2", "customer": "Béla", "total": 5976, "status": "processing"},
    {"order_id": "ORD-3", "customer": "Csilla", "total": 18289, "status": "pending"},
    {"order_id": "ORD-4", "customer": "Dávid", "total": 6786, "status": "completed"},
    {"order_id": "ORD-5", "customer": "Eszter", "total": 12000, "status": "processing"},
]

orders_list = []

sorted_orders = sorted(orders, key=itemgetter('status'))

for status, group in groupby(sorted_orders, key=itemgetter('status')):
    group_orders = list(group)

    orders_list.append({
        "status": status,
        "count": len(group_orders),
        "total": sum(order["total"] for order in group_orders)
    })

print(orders_list)