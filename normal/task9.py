import math

def cyclic_subgroup_in_Zm_additive(N: int) -> dict:
    """
    В аддитивной группе Z_m находит циклическую подгруппу, порождённую элементом t mod m.
    Определяет её порядок и все порождающие элементы.
    """
    m = 4 + (N % 5)
    t_values = [9, 8, 7, 12, 14]
    t = t_values[N % 5] % m
    
    subgroup = set()
    current = 0
    for i in range(m):
        element = (current + t) % m
        subgroup.add(element)
        current = element
    
    order = len(subgroup)
    
    generators = []
    for elem in subgroup:
        if math.gcd(elem, m) == order:
            generators.append(elem)
    
    return {
        "m": m,
        "t": t,
        "subgroup": sorted(subgroup),
        "order": order,
        "generators": generators
    }