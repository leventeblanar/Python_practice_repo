from itertools import chain, islice, groupby
from operator import itemgetter

orders_a = ["ORD-1", "ORD-2"]
orders_b = ["ORD-3", "ORD-4"]

# chain
all_orders = list(chain(orders_a, orders_b))
print(all_orders)

# isslice
orders = ["ORD-1", "ORD-2", "ORD-3", "ORD-4"]
print(list(islice(orders, 2)))

# groupby
orders = [
    {"order_id": "ORD-1", "status": "completed"},
    {"order_id": "ORD-2", "status": "processing"},
    {"order_id": "ORD-3", "status": "completed"},
    {"order_id": "ORD-4", "status": "pending"},
]

sorted_orders = sorted(orders, key=itemgetter("status"))
for status, group in groupby(sorted_orders, key=itemgetter("status")):
    group_orders = list(group)
    print(status, group_orders)