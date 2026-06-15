rows = [
    {"country": "Hungary", "amount": 100},
    {"country": "Germany", "amount": 200},
    {"country": "Hungary", "amount": 50},
]


def dict_grouping():

    summed_results = {}

    for row in rows:
        country = row["country"]
        amount = row["amount"]

        if country not in summed_results:
            summed_results[country] = 0
        
        summed_results[country] += amount
            

    print(summed_results)


def dict_grouping_2():

    sales = [
    {"country": "Hungary", "amount": 120},
    {"country": "Germany", "amount": 200},
    {"country": "Hungary", "amount": 80},
    {"country": "Austria", "amount": 50},
    {"country": "Germany", "amount": 100},
    ]

    summed_sales = {}

    for row in sales:
        country = row["country"]
        amount = row["amount"]

        if country not in summed_sales:
            summed_sales[country] = {"total_amount": 0, "counter": 0, "average_amount": 0}

        summed_sales[country]["total_amount"] += amount
        summed_sales[country]["counter"] += 1

    for row in summed_sales:
        print(row)

    return summed_sales

print(dict_grouping_2())