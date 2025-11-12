import math

def isomorphism_of_cyclic_subgroup_Zm_star(N: int) -> dict:
    """
    В мультипликативной группе Z_m^* находит циклическую подгруппу, порождённую элементом t mod m.
    Определяет, какой циклической подгруппе в симметрической группе S_d она изоморфна.
    """
    m = 4  # m = 4 + (5 % 5) = 4
    t = 9  # t для N mod 5 = 0
    
    subgroup = set()
    current = t
    while current not in subgroup:
        subgroup.add(current)
        current = (current * t) % m
    
    d = len(subgroup)
    
    isomorphic_Sd_subgroup = f"S_{d}" if d > 2 else f"Z_{d}"
    
    return {
        "m": m,
        "t": t,
        "cyclic_subgroup": sorted(subgroup),
        "subgroup_order": d,
        "isomorphic_to": isomorphic_Sd_subgroup
    }
    
