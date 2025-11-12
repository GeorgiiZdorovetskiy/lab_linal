from sympy import symbols, Poly, invert
from sympy.polys.domains import FF

def polynomial_inverse(N: int) -> dict:
    """
    Находит обратный элемент f^{-1} mod g в кольце полиномов над полем F_13
    """
    N_mod = 505285
    s_coeffs = [(t + N_mod) % 11 for t in range(3)]
    
    x = symbols('x')
    
    f = Poly(s_coeffs[2] * x**2 + s_coeffs[1] * x + s_coeffs[0], x)
    g = Poly(x**8 + x**4 + x**3 + 6*x + 2, x)
    
    try:
        inverse = invert(f, g, modulus=13)
        verification = (f * inverse) % g
    except:
        inverse = "Не существует"
        verification = "Не проверяется"
    
    return {
        "f(x)": str(f),
        "g(x)": str(g),
        "f^{-1} mod g": str(inverse),
        "verification": str(verification)
    }
