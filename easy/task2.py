from typing import List, Tuple

def is_palindrom(n: int) -> bool:
    """Проверяет, является ли число палиндромом"""
    num_str = str(n)
    return num_str == num_str[::-1]

def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def circular_permutations(s: str) -> List[str]:
    """Генерирует все циклические перестановки строки"""
    return [s[i:] + s[:i] for i in range(len(s))]

def palindromic_cubes_and_palindromic_primes() -> Tuple[List[int], List[int]]:
    """Находит палиндромы с палиндромными кубами и палиндромные простые числа"""
    result_cubes = []
    result_primes = []
    
    # Поиск палиндромов с палиндромными кубами
    for x in range(10**5):
        cube_value = x ** 3
        if is_palindrom(cube_value):
            result_cubes.append(x)
    
    # Поиск палиндромных простых чисел
    for x in range(2, 10001):
        if is_palindrom(x) and is_prime(x):
            result_primes.append(x)
    
    return result_cubes, result_primes
    
            

