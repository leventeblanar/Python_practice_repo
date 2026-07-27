import logging
from pathlib import Path
import json


# logging.basicConfig(level=logging.INFO)

# logging.info("Pragram elindult")
# logging.warning("Ez egy figyelmeztetés")
# logging.error("Ez egy hiba")

def load_orders(file_path: Path) -> list[dict]:
    logging.info("Orders JSON beolvasása indul")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        logging.error("Hibás JSON formátum")
        return []

    orders = data["orders"]

    logging.info(f"Beolvasott orderek száma: {len(orders)}")

    return orders
