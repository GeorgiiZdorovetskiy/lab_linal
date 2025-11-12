from typing import List, Tuple
from sympy import isprime, primerange

def twin_primes_analysis(limit_pairs: int = 1000) -> Tuple[List[Tuple[int, int]], List[float]]:
    """Анализирует пары простых-близнецов и их распределение"""
    twin_primes = []
    ratio_values = []
    
    # Генерируем простые числа
    primes = list(primerange(2, 2000000))
    primes_set = set(primes)
    
    # Находим пары близнецов
    for p in primes:
        if (p + 2) in primes_set:
            twin_primes.append((p, p + 2))
            if len(twin_primes) >= limit_pairs:
                break
    
    # Вычисляем отношения количества пар близнецов к общему числу простых
    for pair in twin_primes:
        n = pair[1]
        twins_count = sum(1 for a, b in twin_primes if b <= n)
        primes_count = sum(1 for prime in primes if prime <= n)
        ratio_values.append(twins_count / primes_count)
    
    return twin_primes, ratio_values


