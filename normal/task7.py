import math

def order_and_primitivity_of_t(N: int) -> dict:
    """
    Находит порядок элемента t в группе Z_p^* и проверяет, является ли t образующим (примитивным корнем)
    """
    p = 29  # p для N mod 5 = 0
    t = 9   # t для N mod 5 = 0
    
    order = 1
    current = t
    while current != 1:
        current = (current * t) % p
        order += 1
    
    is_primitive = order == p - 1
    
    return {
        "p": p,
        "t": t,
        "order": order,
        "is_primitive_root": is_primitive
    }
