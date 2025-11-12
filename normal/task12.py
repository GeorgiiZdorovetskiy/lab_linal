from sympy import symbols, Poly, factor
from sympy.polys.domains import FF

def polynomial_factorization(N: int) -> dict:
    """
    Исследует полиномы на приводимость и разлагает приводимые полиномы на неприводимые множители:
    - f(x) = x^5 + ∑ c_i x^i в F_5[x]
    - f(x) = x^4 + ∑ d_i x^i в F_9[x]
    """
    c_coeffs = [(k + N) % 5 for k in range(6)]
    d_coeffs = [(l + N) % 9 for l in range(5)]
    
    x = symbols('x')
    
    poly1 = Poly(sum(c_coeffs[i] * x**i for i in range(6)), x)
    poly2 = Poly(sum(d_coeffs[i] * x**i for i in range(5)), x)
    
    factors_F5 = factor(poly1, modulus=5)
    factors_F9 = factor(poly2, modulus=9)
    
    is_irreducible_F5 = factors_F5.is_irreducible
    is_irreducible_F9 = factors_F9.is_irreducible
    
    return {
        "polynomial_1": str(poly1),
        "polynomial_2": str(poly2),
        "factors_in_F5": str(factors_F5),
        "factors_in_F9": str(factors_F9),
        "is_irreducible_F5": is_irreducible_F5,
        "is_irreducible_F9": is_irreducible_F9
    }