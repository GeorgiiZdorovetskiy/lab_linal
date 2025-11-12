from typing import List
from sympy import symbols, Poly, GF
from sympy.polys.polyroots import roots

def polynomial_roots(N: int) -> dict:
    """
    Находит все корни полиномов в конечных полях:
    - f(x) = x^9 + ∑ a_i x^i в F_4[x]
    - f(x) = ∑ b_i x^i в F_7[x]
    """
    a_coeffs = [(i + N) % 4 for i in range(9)]
    b_coeffs = [(j + N) % 7 for j in range(7)]
    
    x = symbols('x')
    
    poly1 = Poly(sum(a_coeffs[i] * x**i for i in range(9)), x)
    poly2 = Poly(sum(b_coeffs[i] * x**i for i in range(7)), x)
    
    roots_F4 = roots(poly1, modulus=4)
    roots_F7 = roots(poly2, modulus=7)
    
    return {
        "polynomial_1": str(poly1),
        "polynomial_2": str(poly2),
        "roots_in_F4": list(roots_F4.keys()),
        "roots_in_F7": list(roots_F7.keys())
    }