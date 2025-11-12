import math

def order_of_sr(N: int) -> int:
    """
    Находит порядок элемента s^r в группе Z_p^*
    """
    p_values = [29, 31, 37, 23, 19]
    r_values = [59, 60, 38, 45, 44]
    s_values = [5, 4, 3, 17, 15]
    
    p = p_values[N % 5]
    r = r_values[N % 5]
    s = s_values[N % 5]
    
    s_r = pow(s, r, p)
    
    order = 1
    current = s_r
    while current != 1:
        current = (current * s_r) % p
        order += 1
    
    return order