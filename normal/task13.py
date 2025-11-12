from sympy import symbols, Poly, gcdex
from sympy.polys.domains import FF

def polynomial_gcd(N: int) -> dict:
    """
    Находит НОД полиномов f и g и его линейное представление:
    gcd(f,g) = u(x)f(x) + v(x)g(x)
    """
    r_coeffs = [(m + N) % 11 for m in range(8)]
    s_coeffs = [(t + N) % 11 for t in range(4)]
    
    x = symbols('x')
    
    f = Poly(sum(r_coeffs[i] * x**i for i in range(8)), x)
    g = Poly(sum(s_coeffs[i] * x**i for i in range(4)), x)
    
    gcd_poly = f.gcd(g)
    
    u, v, w = gcdex(f, g)
    
    return {
        "f(x)": str(f),
        "g(x)": str(g),
        "gcd(f,g)": str(gcd_poly),
        "u(x)": str(u),
        "v(x)": str(v),
        "verification": f"u*f + v*g = {u*f + v*g}"
    }