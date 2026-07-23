import json
from pathlib import Path

def read_json():

    try:
        with Path("orders.json").open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("hibás JSON formátum")
        
    orders = data["orders"]

    simplified_orders = []

    for index, order in enumerate(orders, 1):
        customer_data = order["customer"]

        simplified_orders.append({
            "row": index,
            "orderId": order['order_id'],
            "customerName": customer_data['name']
        })

    with Path("output.json").open("w", encoding="utf-8") as file:
        json.dump(simplified_orders, file, ensure_ascii=False, indent=4)

    

read_json()