import math

def order_and_primitivity_of_t(N: int) -> dict:
    """
    Находит порядок элемента t в группе Z_p^* и проверяет, является ли t образующим (примитивным корнем)
    """
    p_values = [29, 31, 37, 23, 19]
    t_values = [9, 8, 7, 12, 14]
    
    p = p_values[N % 5]
    t = t_values[N % 5]
    
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