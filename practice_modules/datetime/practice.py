from datetime import datetime, date

orders = [
    {"order_id": "ORD-1", "created_at": "2026-07-20T09:14:32Z", "total": 15480},
    {"order_id": "ORD-2", "created_at": "2026-07-21T13:47:05Z", "total": 5976},
    {"order_id": "ORD-3", "created_at": "2026-07-22T08:02:19Z", "total": 18289},
    {"order_id": "ORD-4", "created_at": "2026-07-23T10:38:12Z", "total": 21807},
]

order_created_at_limit = date(2026, 7, 22)
today = date(2026, 7, 24)

after_limit = []
orders_by_day = {}

for order in orders:
    print(order['order_id'])
    str_created_at = order["created_at"]
    created_at = datetime.fromisoformat(
        str_created_at.replace("Z", "+00:00")
    )
    if isinstance(created_at, datetime):
        print(f"{created_at} -> Sikerült")
    else:
        print(f"{created_at} -> Béna")

    created_at_only_date = created_at.date()
    print(f"Csak a dátum: {created_at_only_date}")
    print("\n")

    date_in_days = today - created_at_only_date

    orders_by_day[created_at_only_date] = str(date_in_days)

    if created_at_only_date >= order_created_at_limit:
        after_limit.append({
            "order_id": order['order_id'],
            "created_at": created_at,
            "old_in_days": date_in_days.days,
        })

print(after_limit)
print(orders_by_day)
