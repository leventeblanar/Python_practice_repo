from pathlib import Path
import json
from json import JSONDecodeError
import logging
from datetime import datetime

def read_json() -> list[dict]:

    logging.info("Orders.json beolvasás...")

    try:
        with Path("orders.json").open("r", encoding="utf-8") as file:
            raw_orders = json.load(file)
    except JSONDecodeError:
        logging.exception("Hibás JSON decodeolás")
        raise
    except FileExistsError:
        logging.error("Nem található az orders.json fájl")
        return []

    orders = raw_orders["orders"]

    logging.info("Orders.json beolvasása sikeres.")

    return orders

def summarize_order(orders: list[dict]) -> list[dict]:

    summerized_orders = []

    for order in orders:

        calculated_total = 0
        created_at = datetime.fromisoformat(order["created_at"].replace("Z", "+00:00"))

        formatted_created_at = created_at.strftime("%Y-%m-%d")

        for item in order["items"]:
            item_line_total = item["line_total"]
            calculated_total += item_line_total

        order_payload = {
            "order_id": order["order_id"],
            "customer_name": order["customer"]["name"],
            "status": order["status"],
            "created_date": formatted_created_at,
            "item_count": len(order["items"]),
            "reported_total": order["total"],
            "calculated_total": calculated_total,
            "total_matches": True if calculated_total == order["total"] else False,
        }

        summerized_orders.append(order_payload)

    return summerized_orders

def main():

    logging.info("Rendelések összegzése process indul... ")
    orders = read_json()
    summerized_orders = summarize_order(orders)
    print(summerized_orders)
    with Path("summerized_order.json").open("w", encoding="utf-8") as output_file:
        json.dump(summerized_orders, output_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()