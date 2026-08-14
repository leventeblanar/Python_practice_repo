from operator import itemgetter, attrgetter
from dataclasses import dataclass

sales = [
    {"country": "Hungary", "amount": 12000},
    {"country": "Germany", "amount": 8000},
    {"country": "Austria", "amount": 5000},
]

def itemgetter_func(): # dict kulcsokhoz
    # Eddig:
    sorted(sales, key=lambda row: row["amount"])

    # operator.itemgetter
    sorted(sales, key=itemgetter("amount"))
    sorted_sales = sorted(sales, key=itemgetter("amount"), reverse=True)
    sorted_sales = sorted(sales, key=itemgetter("country", "amount"))


@dataclass
class Product:
    name: str
    price: int

product = [
    Product("Laptop", 300000),
    Product("Mouse", 8000),
    Product("Monitor"), 90000,
]

def attrgetter_func(): # objektum/dataclass aatribútumokhoz
    sorted_products = sorted(product, key=attrgetter("price"))