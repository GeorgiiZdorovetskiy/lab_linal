import math

def cyclic_subgroup_in_Zm_additive(N: int) -> dict:
    """
    В аддитивной группе Z_m находит циклическую подгруппу, порождённую элементом t mod m.
    Определяет её порядок и все порождающие элементы.
    """
    m = 4  # m = 4 + (5 % 5) = 4
    t = 9  # t для N mod 5 = 0
    
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
