from typing import List
from itertools import product
from sympy import symbols, Poly

def generate_irreducible_polynomials(q: int, d: int) -> list:
    """
    Генерирует все неприводимые полиномы степени d над простым конечным полем F_q
    """
    x = symbols('x')
    irreducible_polys = []
    
    for coeffs in product(range(q), repeat=d+1):
        if coeffs[-1] != 0:
            poly = Poly(sum(coeffs[i] * x**i for i in range(d+1)), x)
            if poly.is_irreducible:
                irreducible_polys.append(str(poly))
    
    return irreducible_polys[:10]