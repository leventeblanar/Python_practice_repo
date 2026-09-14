from functools import partial, lru_cache


# van egy függvényünk -> partial fixál benne egy paramétert -> új callable
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))
print(cube(5))

# emellé létezik az @lru_cache

@lru_cache
def power_cached(base, exponent):
    print("Caclulating...")
    return base ** exponent

print(power_cached(5, 2))
print(power_cached(5, 2))
print(power_cached(5, 3))
print(power.cache_info())