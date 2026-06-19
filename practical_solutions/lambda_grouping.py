def pelda_1():
    
    sales = [
        {"country": "Hungary", "amount": 120},
        {"country": "Germany", "amount": 200},
        {"country": "Austria", "amount": 50},
    ]

    sorted_sales_by_amount = sorted(sales, key=lambda row: row['amount'], reverse=True)
    sorted_sales_by_name = sorted(sales, key=lambda row: row['country'])

    print(sorted_sales_by_name)


def pelda_2():

    country_totals = {
        "Hungary": {"total_amount": 200, "count": 2},
        "Germany": {"total_amount": 300, "count": 2},
        "Austria": {"total_amount": 50, "count": 1},
    }

    items = country_totals.items()

    sorted_countries = sorted(country_totals.items(), key=lambda item: item[1]['total_amount'], reverse=True)

    return sorted_countries

def pelda_3():

    sales = [
        {"country": "Hungary", "amount": 120},
        {"country": "Germany", "amount": 200},
        {"country": "Austria", "amount": 50},
        {"country": "Hungary", "amount": 80},
    ]

    sorted_sales_by_amount_asc = sorted(sales, key=lambda row: row['amount'], reverse=False)
    sorted_sales_by_amount_desc = sorted(sales, key=lambda row: row['amount'], reverse=True)
    sorted_sales_by_country = sorted(sales, key=lambda row: row['country'])
    biggest_sale = sorted_sales_by_amount_desc[0]

    print(sorted_sales_by_amount_asc)
    print(sorted_sales_by_amount_desc)
    print(sorted_sales_by_country)
    print(biggest_sale)

pelda_3()