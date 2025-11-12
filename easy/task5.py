from typing import Dict
from sympy import factorial, factorint

def factorial_plus_one_factors() -> Dict[int, Dict[int, int]]:
    """Вычисляет разложение n! + 1 на простые множители"""
    result_data = {}
    
    for n in range(2, 51):
        value = factorial(n) + 1
        factors = factorint(value)
        result_data[n] = factors
    
    return result_data

if __name__ == "__main__":
    data = factorial_plus_one_factors()
    
    # Вывод первых нескольких результатов
    for n in range(2, 11):
        print(f"{n}! + 1 = {data[n]}")
    
    # Анализ максимального количества различных простых делителей
    max_factors_count = max(len(factors) for factors in data.values())
    n_with_max = [n for n, factors in data.items() if len(factors) == max_factors_count]
    
    print(f"\nМаксимальное количество различных простых делителей: {max_factors_count}")
    print(f"Для n = {n_with_max}")
    
    # Поиск случаев с большими простыми множителями
    big_prime_cases = {
        n: [p for p in factors.keys() if p > 10**6]
        for n, factors in data.items()
        if any(p > 10**6 for p in factors)
    }
    
    print("\nСлучаи с большими простыми множителями (> 10^6):")
    for n, primes in big_prime_cases.items():
        print(f"n = {n}: {primes}")