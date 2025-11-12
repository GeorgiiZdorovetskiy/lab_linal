import time
from typing import List, Dict
import math
from sympy import totient, factorint

def euler_phi_direct(n: int) -> int:
    """Вычисляет φ(n) методом прямого перебора"""
    count = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            count += 1
    return count

def euler_phi_factor(n: int) -> int:
    """Вычисляет φ(n) через разложение на простые множители"""
    if n <= 0:
        return 0
    
    result = n
    factors = factorint(n)
    
    for p in factors:
        result = result * (p - 1) // p
    
    return result

def compare_euler_phi_methods(test_values: List[int]) -> Dict[str, List[float]]:
    """Сравнивает время выполнения разных методов вычисления φ(n)"""
    timings = {
        'direct': [],
        'factor': [], 
        'sympy': []
    }
    
    for n in test_values:
        # Прямой перебор
        start = time.time()
        euler_phi_direct(n)
        timings['direct'].append(time.time() - start)
        
        # Через разложение на множители
        start = time.time()
        euler_phi_factor(n)
        timings['factor'].append(time.time() - start)
        
        # Встроенная функция sympy
        start = time.time()
        totient(n)
        timings['sympy'].append(time.time() - start)
    
    return timings

if __name__ == "__main__":
    test_vals = [10000, 50000, 100000, 200000]
    timings = compare_euler_phi_methods(test_vals)
    
    for method, times in timings.items():
        print(f"Метод {method}:")
        for n, t in zip(test_vals, times):
            print(f"  n={n:<7} => {t:.6f} сек")