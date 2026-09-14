from functools import lru_cache

@lru_cache(maxsize=10)
def calculate_discount(price, percent):
    print("Calculating...")
    return price - (price * (percent / 100))

print(calculate_discount(10, 15))
print(calculate_discount(10, 15))
print(calculate_discount(10, 15))