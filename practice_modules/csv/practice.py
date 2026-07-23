import csv
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Order:
    id: int
    customer: str | None
    amount: int
    country: str

def parse_order(row: dict) -> Order | None:
    try:
        return Order(
            id=int(row["id"]),
            customer=row["customer"],
            amount=int(row["amount"]),
            country=row["country"],
        )
    except ValueError:
        return None

def load_orders(file_path: Path) -> list[Order]:
    orders = []

    with file_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            order = parse_order(row)

            if order is None:
                print("Invalid CSV row, unable to parse.")
                continue
            
            orders.append(order)

    return orders

def write_invalid_orders(file_path: Path, invalid_orders: list[dict]):
    fieldnames = [
        "row",
        "order_id",
        "customer",
        "amount",
        "country",
        "errors"
    ]

    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for item in invalid_orders:
            order = item["order"]
            errors = item["errors"]

            writer.writerow({
                "row": item["row"],
                "order_id": order.id,
                "customer": order.customer,
                "amount": order.amount,
                "country": order.country,
                "errors": ", ".join(errors),
            })


def validate_orders(orders: list[Order]) -> tuple[list[dict], list[dict]]:

    valid_orders = []
    invalid_orders = []

    for index, order in enumerate(orders, 1):
        errors = []

        if not order.customer:
            errors.append("Missing customer name.")
        if order.amount <= 0:
            errors.append("Invalid price")

        if errors:
            invalid_orders.append({
                "row": index,
                "order": order,
                "errors": errors
            })
        else:
            valid_orders.append({
                "row": index,
                "order": order,
            })

    return valid_orders, invalid_orders


def main() -> None:

    input_file_path = Path("orders.csv")
    output_file_path = Path("invalid_orders.csv")

    orders = load_orders(input_file_path)
    valid_orders, invalid_orders = validate_orders(orders)

    write_invalid_orders(output_file_path, invalid_orders)

    print(f"Valid orders: {len(valid_orders)}")
    print(f"Invalid orders: {len(invalid_orders)}")


if __name__ == "__main__":
    main()
