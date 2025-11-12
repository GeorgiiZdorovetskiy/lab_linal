from typing import Dict, List, Tuple, Set
import random
from itertools import permutations

Permutation = Tuple[int, ...]
Group = List[Permutation]
Subgroup = Set[Permutation]

def _compose(p: Permutation, q: Permutation) -> Permutation:
    """Композиция p∘q (сначала q, потом p)."""
    return tuple(p[q[i]] for i in range(len(p)))

def _identity(m: int) -> Permutation:
    """Единичная перестановка."""
    return tuple(range(m))

def _power(p: Permutation, k: int) -> Permutation:
    """Возвращает p^k (итеративное применение композиции)."""
    result = _identity(len(p))
    for _ in range(k):
        result = _compose(result, p)
    return result

def _order_of_element(p: Permutation) -> int:
    """Порядок элемента: минимальное n > 0, такое что p^n = e."""
    e = _identity(len(p))
    q = p
    n = 1
    while q != e:
        q = _compose(q, p)
        n += 1
    return n

def _all_permutations(m: int) -> Group:
    """Возвращает список всех перестановки S_m."""
    return list(permutations(range(m)))

def element_powers_in_Sm(N: int) -> dict:
    """
    В группе S_m берётся элемент g с индексом N mod |S_m|.
    Вычисляются порядки элементов g^n1, g^n2, g^n3
    и порядки циклических подгрупп, ими порождаемых.
    """
    m = 4  # m = 4 + (5 % 5) = 4
    n1 = 5  # n1 = 5 % 6 = 5
    n2 = 0  # n2 = (5 + 1) % 6 = 0
    n3 = 1  # n3 = (5 + 2) % 6 = 1
    
    G = _all_permutations(m)
    group_order = len(G)

    idx = 5 % group_order  # N = 5
    g = G[idx]

    result = {
        "m": m,
        "group_order": group_order,
        "element_index": idx,
        "element": g,
        "n1": n1, "n2": n2, "n3": n3,
        "powers": []
    }

    for n in [n1, n2, n3]:
        g_power = _power(g, n)
        order_elem = _order_of_element(g_power)
        order_subgroup = order_elem

        result["powers"].append({
            "n": n,
            "g^n": g_power,
            "order_of_element": order_elem,
            "order_of_subgroup": order_subgroup
        })

    return result
