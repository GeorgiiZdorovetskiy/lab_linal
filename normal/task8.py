import math

def generators_of_Zm_star(N: int) -> list:
    """
    Находит все образующие (примитивные корни) циклической группы Z_m^*
    """
    m = 4  # m = 4 + (5 % 5) = 4
    
    generators = []
    for g in range(1, m):
        if math.gcd(g, m) == 1:
            order = 1
            current = g
            while current != 1:
                current = (current * g) % m
                order += 1
            if order == len([i for i in range(1, m) if math.gcd(i, m) == 1]):
                generators.append(g)
    
    return generators
