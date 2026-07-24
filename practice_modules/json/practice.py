import json
from pathlib import Path

input_file_path = Path("orders.json")
output_file_path = Path("order_summary.json")

def load_json(file_path: Path):

    try:
        with file_path.open("r", encoding="utf-8") as input_file:
            data = json.load(input_file)
    except json.JSONDecodeError:
        print("Hibás JSON file.")
        return []

    return data["orders"]

def main():
    orders = load_json(input_file_path)

    osszes_order = len(orders)

    print(f"Összes order száma: {osszes_order}")
    print(f"Első order id: {orders[0]['order_id']}")
    print(f"Első customer neve: {orders[0]['customer']['name']}")

    order_summary = []

    for order in orders:
        items = order["items"]
        item_total = 0
        for item in items:
            item_total = item_total + item['line_total'] 

        order_summary.append({
            "order_id": order['order_id'],
            "customer_name": order['customer']['name'],
            "status": order['status'],
            "total": item_total,
            "item_count": len(items)
        })

    with output_file_path.open("w", encoding="utf-8") as output_file:
        json.dump(order_summary, output_file, ensure_ascii=False, indent=4)    

if __name__ == "__main__":
    main()