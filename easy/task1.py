from typing import List, Tuple

def is_palindrom(n: int) -> bool:
    """Проверяет, является ли число палиндромом"""
    num_str = str(n)
    return num_str == num_str[::-1]

def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def circular_permutations(s: str) -> List[str]:
    """Генерирует все циклические перестановки строки"""
    permutations_list = []
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        permutations_list.append(rotated)
    return permutations_list

def palindromic_squares_and_circular_primes() -> Tuple[List[int], List[int]]:
    """Находит палиндромы с палиндромными квадратами и циклические простые числа"""
    # Поиск палиндромов с палиндромными квадратами
    palindromic_squares = []
    for a in range(1, 10**5):
        if is_palindrom(a) and is_palindrom(a * a):
            palindromic_squares.append(a)
    
    # Поиск циклических простых чисел
    circular_primes = []
    for p in range(2, 10**6):
        if is_prime(p):
            digit_string = str(p)
            rotations = circular_permutations(digit_string)
            if all(is_prime(int(rot)) for rot in rotations):
                circular_primes.append(p)
    
    return palindromic_squares, circular_primes



