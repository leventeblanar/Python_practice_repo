from collections import defaultdict, Counter

def pelda_1():
    sales = [
        {"country": "Hungary", "amount": 120},
        {"country": "Germany", "amount": 200},
        {"country": "Hungary", "amount": 80},
    ]

    country_totals = defaultdict(int)

    for row in sales:
        country = row['country']
        amount = row['amount']

        country_totals[country] += amount

    grouped_sales = defaultdict(list)

    for row in sales:
        country = row["country"]

        grouped_sales[country].append(row)

    print(grouped_sales)

def pelda_2():

    sales = [
        {"country": "Hungary", "amount": 120},
        {"country": "Germany", "amount": 200},
        {"country": "Hungary", "amount": 80},
        {"country": "Austria", "amount": 50},
        {"country": "Germany", "amount": 100},
    ]

    country_totals = defaultdict(int)
    lines_by_country = defaultdict(list)
    country_counts = Counter()

    for row in sales:
        country = row["country"]
        amount = row['amount']

        country_totals[country] += amount
        lines_by_country[country].append(row)
        country_counts[country] += 1
    
    print(country_totals)
    print(lines_by_country)
    print(country_counts)

pelda_2()