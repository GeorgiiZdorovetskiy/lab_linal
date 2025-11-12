from typing import List, Set
import math

def _get_divisors(n: int) -> List[int]:
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def _cyclic_subgroup(g: int, m: int) -> Set[int]:
    subgroup = set()
    current = g
    while current not in subgroup:
        subgroup.add(current)
        current = (current * g) % m
    return subgroup

def subgroups_of_Zm_star(N: int) -> list:
    """
    Находит все подгруппы мультипликативной группы Z_m^*
    """
    m = 4 + (N % 5)
    
    Zm_star = [i for i in range(1, m) if math.gcd(i, m) == 1]
    phi_m = len(Zm_star)
    
    all_subgroups = []
    for g in Zm_star:
        subgroup = _cyclic_subgroup(g, m)
        if subgroup not in all_subgroups:
            all_subgroups.append(subgroup)
    
    return [list(subgroup) for subgroup in all_subgroups]