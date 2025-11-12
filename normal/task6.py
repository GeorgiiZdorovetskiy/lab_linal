import math

def order_of_sr(N: int) -> int:
    """
    Находит порядок элемента s^r в группе Z_p^*
    """
    p = 29  # p для N mod 5 = 0
    r = 59  # r для N mod 5 = 0
    s = 5   # s для N mod 5 = 0
    
    s_r = pow(s, r, p)
    
    order = 1
    current = s_r
    while current != 1:
        current = (current * s_r) % p
        order += 1
    
    return order
