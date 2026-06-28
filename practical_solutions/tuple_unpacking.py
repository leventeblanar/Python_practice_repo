def tuple_unpacking():
    
    sales_summary = [
        ("Hungary", 200),
        ("Germany", 300),
        ("Austria", 50),
    ]

    for country, amount in sales_summary:
        print(f"Ország: {country} | Eladás: {amount}")

tuple_unpacking()