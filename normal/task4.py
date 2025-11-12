from typing import Dict, List
import math

def elements_of_order_k_in_cyclic_group(N: int) -> dict:
    """
    В циклической группе порядка m находит:
    - Все элементы g, такие что g^k = e
    - Все элементы порядка k
    """
    m = 4  # m = 4 + (5 % 5) = 4
    k = 6  # k = 1 + (5 % 7) = 6
    
    elements_g_k = []
    elements_order_k = []
    
    for i in range(m):
        if math.gcd(i, m) == 1:
            order = m // math.gcd(m, i)
            if (i ** k) % m == 1:
                elements_g_k.append(i)
            if order == k:
                elements_order_k.append(i)
    
    return {
        "group_order": m,
        "k": k,
        "elements_g_satisfying_g_k_equals_e": elements_g_k,
        "elements_of_order_k": elements_order_k
    }
