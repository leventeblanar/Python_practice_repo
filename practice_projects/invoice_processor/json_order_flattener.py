import json
from pathlib import Path
from datetime import datetime
import shutil

from json import JSONDecodeError


INPUT_PATH = Path(__file__).resolve().parent / "src"
OUTPUT_PATH = Path(__file__).resolve().parent / "output"
PROCESSED_FOLDER_PATH = Path(__file__).resolve().parent / "processed_orders"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
PROCESSED_FOLDER_PATH.mkdir(parents=True, exist_ok=True)

SOURCE_FILE = INPUT_PATH / "orders.json"
OUTPUT_FILE = OUTPUT_PATH / "flattened_orders.json"

def flatten_orders(orders: list[dict]) -> list[dict]:
    if not orders:
        return []

    flattened_orders = []

    for order in orders:
        created_at_raw = order["created_at"]
        created_at = datetime.fromisoformat(created_at_raw.replace("Z", "+00:00")).strftime("%Y%m%d_%H%M")
        customer_data = order["customer"]
        shipping_data = order["shipping"]

        for item in order["items"]:
            flattened_order = {
                "order_id": order["order_id"],
                "created_at": created_at,
                "status": order["status"],
                "customer_id": customer_data["id"],
                "customer_name": customer_data["name"],
                "customer_email": customer_data["email"],
                "shipping_method": shipping_data["method"],
                "shipping_address": shipping_data["address"] or None,
                "sku": item["sku"],
                "item_name": item["name"],
                "quantity": item["quantity"],
                "unit_price": item["unit_price"],
                "line_total": item["line_total"],
            }

            flattened_orders.append(flattened_order)

    return flattened_orders


def main():

    try:
        with SOURCE_FILE.open("r", encoding="utf-8") as file:
            raw_orders = json.load(file)
            orders = raw_orders["orders"]
            print("Sikeres orders.json beolvasás...")
    except JSONDecodeError:
        print("Sikertelen orders.json beolvasás.")
        raise

    flattened_orders = flatten_orders(orders)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file_output:
        json.dump(flattened_orders, file_output, ensure_ascii=False, indent=4)
    print("Sikeres flattened_orders.json kiírás...")

    processed_file = PROCESSED_FOLDER_PATH / SOURCE_FILE.name
    shutil.move(SOURCE_FILE, processed_file)
    print("orders.json processed mappába áthelyezve...")

if __name__ == '__main__':
    main()