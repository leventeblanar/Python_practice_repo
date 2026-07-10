def feladat_1_2():

    users = [
    {"id": 1, "name": "Anna", "role": "admin"},
    {"id": 2, "name": "Béla", "role": "developer"},
    {"id": 3, "name": "Csilla", "role": "viewer"},
    ]

    users_by_id = {}

    for user in users:
        user_id = user['id']
        users_by_id[user_id] = user

    print(users_by_id[2]['name'])

    users_by_id[2].update({"role": "senior developer", "active": True})

    print(users_by_id[2])

def feladat_3():

    system_ids = [1, 2, 3, 4]
    incoming_ids = [2, 3, 99]

    system_ids_set = set(system_ids)
    incoming_ids_set = set(incoming_ids)

    diffs = incoming_ids_set - system_ids_set

    print(diffs)

def feladat_4():

    products = [
    {"name": "Laptop", "price": 300000},
    {"name": "", "price": 150000},
    {"name": "Mouse", "price": 8000},
    {"name": "Keyboard", "price": 0},
    ]

    hibas_sorok = []
    jo_sorok = []

    for index, product in enumerate(products, 1):

        errors = []

        if not product['name']:
            errors.append("Hiányzó név")
        if product['price'] <= 0:
            errors.append("Hibás ár")
            
        if errors:
            hibas_sorok.append({
                "row": index,
                "errors": errors
            })
        else:
            jo_sorok.append({
                "row": index,
                "info": product
            })

    print(hibas_sorok)
    print(jo_sorok)