from typing import Dict, List, Tuple
from itertools import product
from sympy import isprime

def primes_with_two_digits() -> Dict[str, List[int]]:
    """Находит простые числа для указанных пар цифр"""
    result_dict = {}
    digit_combinations = {
        '13': ['1', '3'],
        '15': ['1', '5'],
        '17': ['1', '7'], 
        '19': ['1', '9']
    }
    
    for key, digits in digit_combinations.items():
        primes_list = []
        current_length = 1
        
        while len(primes_list) < 100:
            # Генерируем все комбинации текущей длины
            for comb in product(digits, repeat=current_length):
                if comb[0] == '0':
                    continue
                number = int(''.join(comb))
                if isprime(number):
                    primes_list.append(number)
                    if len(primes_list) == 100:
                        break
            current_length += 1
        
        result_dict[key] = primes_list
    
    return result_dict



